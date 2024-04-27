# -*- coding: utf-8 -*-
"""
ENV variables

   export torch_device='cpu'



### How to run
    sudo docker run -d -p 6333:6333     -v ~/.watchtower/qdrant_storage:/qdrant/storage:z     qdrant/qdrant





### Benchmarks:
    alias py2="python engine.py "

    py2 bench_v1_create_indexes --dirdata_root ztmp/bench/
    py2 bench_v1_run  --dirout ztmp/bench/   --topk 5


    ### Bench
       tantivy : v1  6ms
       Sparse :      23ms
       Dense:        30 ms




### Benchmark accuracy: 
   Sames 1000 query for all 3.
     --> Accuracy.
     --> Compare the errors.

     join the dataframe on id


     ### csv metrics
       df1 = df1.merge(df2, on='id', how='left', suffixes=('', '_2'))

       df[ df.is_topk == 0 ] --> Find errors.




"""

import os, pathlib, uuid, time, traceback
from typing import Any, Callable, Dict, List, Optional, Sequence, Union

from box import Box  ## use dot notation as pseudo class

import pandas as pd, numpy as np, torch
import tantivy

from fastembed import TextEmbedding

from qdrant_client import QdrantClient
from qdrant_client import models
from qdrant_client.http.models import PointStruct

# from fastembed import TextEmbedding
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForMaskedLM, TransfoXLCorpus
from ranx import Qrels, Run, fuse


from utilmy import pd_read_file, os_makedirs, pd_to_file, date_now, glob_glob
from utilmy import log, log2

from .engine import (EmbeddingModel, EmbeddingModelSparse, dataset_hf_to_parquet, qdrant_dense_create_index, qdrant_dense_search,
   dataset_hf_to_parquet, dataset_agnews_schema_v1,
   qdrant_sparse_create_index, qdrant_sparse_search, qdrant_dense_create_collection, qdrant_sparse_create_collection, qdrant_collection_exists, 
   tantivy_index_documents, EmbeddingModelSparse, tantivy_search
)


##########################################################################################
def np_random_subset(txt:str, size=100):
    i1 = np.random.randint(0, len(txt)-size)
    return txt[i1 : i1+size]


def check_error(dirin):
    df1 = pd_read_file(f"{dirin}/bench/.csv")
    df2 = pd_read_file(f"{dirin}/bench/.csv")
    df3 = pd_read_file(f"{dirin}/bench/.csv")

    df1 = df1.merge(df2, on="id", how="left", suffixes=("", "_2"))
    df1 = df1.merge(df3, on="id", how="left", suffixes=("", "_3"))




def bench_v1_dense_run(cfg=None, dirout="zmtp/bench/", topk=5):
    """Measure performance in Real and bigger dataset.

    python engine.py bench_v1_run  --dirout ztmp/bench/   --topk 5


    """
    # create query df in ztmp directory
    dataset = "ag_news"
    collection_name = f"hf-{dataset}-dense"
    dirtmp = f"{dirout}/{dataset}/df_search_test.parquet"

    if not os.path.exists(dirtmp):
        df = pd_read_file(f"{dirout}/norm/{dataset}/*/df_0.parquet")  ##  Real Dataset
        # pick thousand random rows
        df_query = df.sample(1000)
        pd_to_file(df_query, dirtmp)
    else:
        df_query = pd_read_file(dirtmp)

    model_type = "stransformers"
    model_id = "sentence-transformers/all-MiniLM-L6-v2"  ### 384,  50 Mb
    model = EmbeddingModel(model_id, model_type)

    cc = Box({})
    cc.metrics = []

    for i, row in df_query.iterrows():
        # print(row)
        id1 = row["id"]
        query = row["body"][:300]

        t0 = time.time()
        results = qdrant_dense_search(
            query, collection_name=collection_name, model=model, topk=topk
        )
        dt = time.time() - t0
        top_5 = [scored_point.id for scored_point in results[:topk]]

        #### Accuracy.abs
        istop_k = 1 if id1 in top_5 else 0
        cc.metrics.append([id1, istop_k, dt])

    tunix = date_now(fmt="%Y%m%d_%H%M_%S", returnval="str")
    dirout2 = f"{dirout}/{dataset}/dense/{tunix}/"
    dfmetrics = pd.DataFrame(cc.metrics, columns=["id", "istop_k", "dt"])
    pd_to_file(dfmetrics, f"{dirout2}/dfmetrics.csv", show=1)
    log(" Avg time per request", dfmetrics["dt"].mean())


def bench_v1_create_dense_indexes(dirdata_root="ztmp/bench"):
    """Create indexes for benchmarking
    python engine.py bench_v1_create_indexes --dirout ztmp/bench/
    """
    # download dataset from Hugging Face in dirout
    # save normalized dataset in dirout/norm
    dataset = "ag_news"
    model_type = "stransformers"
    model_id = "sentence-transformers/all-MiniLM-L6-v2"  ### 384,  50 Mb

    dirdata_norm = f"{dirdata_root}/norm/{dataset}"
    # print(filelist)
    collection_name = f"hf-{dataset}-dense"
    qclient = QdrantClient("http://localhost:6333")
    if qdrant_collection_exists(qclient, collection_name):
        log(f"collection {collection_name} already exists")
        return

    dataset_hf_to_parquet("ag_news", dirout=dirdata_root, splits=["train", "test"])
    # normalize
    dataset_agnews_schema_v1(
        dirin=f"{dirdata_root}/{dataset}/*.parquet", dirout=dirdata_norm
    )
    model = EmbeddingModel(model_id, model_type)

    qdrant_dense_create_collection(
        q_client=qclient, collection_name=collection_name, size=model.model_size
    )
    qdrant_dense_create_index(
        dirin=f"{dirdata_norm}/*/*.parquet",
        collection_name=collection_name,
        coltext="body",
        colscat=["title", "body", "cat1"],
        model_id="sentence-transformers/all-MiniLM-L6-v2",
        model_type="stransformers",
        batch_size=100,
    )


def bench_v1_create_tantivy_indexes(dirdata_root="ztmp/bench"):
    """Create indexes for benchmarking
    python engine.py bench_v1_create_tantivy_indexes --dirout ztmp/bench/
    """
    # download dataset from Hugging Face in dirout
    # save normalized dataset in dirout/norm
    dataset = "ag_news"

    dirdata_norm = f"{dirdata_root}/norm/{dataset}"
    # print(filelist)
    index_path = f"{dirdata_root}/tantivy_index/hf-{dataset}"
    if os.path.exists(index_path):
        return

    dataset_hf_to_parquet("ag_news", dirout=dirdata_root, splits=["train", "test"])
    # normalize

    dataset_agnews_schema_v1(
        dirin=f"{dirdata_root}/{dataset}/*.parquet", dirout=dirdata_norm
    )
    colsused = ["title", "body", "cat1"]
    tantivy_index_documents(
        dirin=f"{dirdata_norm}/*/*.parquet", datapath=index_path, colsused=colsused
    )


def bench_v1_tantivy_run(cfg=None, dirout="ztmp/bench", topk=5):
    """Measure performance in Real and bigger dataset.

    python engine.py bench_v1_tantivy_run  --dirout ztmp/bench/   --topk 5

    """
    # create query df in ztmp directory
    dataset = "ag_news"
    datapath = f"{dirout}/tantivy_index/hf-{dataset}"
    dirtmp = f"{dirout}/{dataset}/query/df_search_test.parquet"

    if not os.path.exists(dirtmp):
        df = pd_read_file(f"{dirout}/norm/{dataset}/*/df_0.parquet")  ##  Real Dataset
        # pick thousand random rows
        df_query = df.sample(1000)
        pd_to_file(df_query, dirtmp)
    else:
        df_query = pd_read_file(dirtmp)

    cc = Box({})
    cc.metrics = []

    for i, row in df_query.iterrows():
        # print(row)
        id1 = row["id"]
        title = row["title"]
        query = row["body"][:300]

        # clean query to avoid query language errors
        # replace non alphanumeric characters with space
        query = "".join([c if c.isalnum() else " " for c in query])
        t0 = time.time()
        results = tantivy_search(datapath=datapath, query=query, topk=topk)
        dt = time.time() - t0

        # tantivy returning id as float, hence using title instead
        top_5_titles = [doc["title"][0] for score, doc in results]
        # log(top_5_titles)
        #### Accuracy.abs
        istop_k = 1 if title in top_5_titles else 0
        cc.metrics.append([id1, istop_k, dt])

    tunix = date_now(fmt="%Y%m%d_%H%M_%S", returnval="str")
    dirout2 = f"{dirout}/{dataset}/tantivy/{tunix}/"
    dfmetrics = pd.DataFrame(cc.metrics, columns=["id", "istop_k", "dt"])
    pd_to_file(dfmetrics, f"{dirout2}/dfmetrics.csv", show=1)
    log(" Avg time per request", dfmetrics["dt"].mean())


def bench_v1_create_sparse_indexes(dirdata_root="ztmp/bench"):
    dataset = "ag_news"
    model_id = "naver/efficient-splade-VI-BT-large-query"  # 17.7 MB
    dirdata_norm = f"{dirdata_root}/norm/{dataset}"
    # print(filelist)
    collection_name = f"hf-{dataset}-sparse"
    qclient = QdrantClient("http://localhost:6333")
    if qdrant_collection_exists(qclient, collection_name):
        log(f"collection {collection_name} already exists")
        return

    # if dirdata_norm not empty skip
    norm_files = glob_glob(f"{dirdata_norm}/*/*.parquet")
    if len(norm_files) == 0:
        dataset_hf_to_parquet("ag_news", dirout=dirdata_root, splits=["train", "test"])
        # normalize
        dataset_agnews_schema_v1(
            dirin=f"{dirdata_root}/{dataset}/*.parquet", dirout=dirdata_norm
        )

    qdrant_sparse_create_collection(q_client=qclient, collection_name=collection_name)
    qdrant_sparse_create_index(
        dirin=f"{dirdata_norm}/*/*.parquet",
        collection_name=collection_name,
        coltext="body",
        colscat=["title", "body", "cat1"],
        model_id=model_id,
        batch_size=10,
    )


def bench_v1_sparse_run(cfg=None, dirout="ztmp/bench", topk=5):
    """Measure performance in Real and bigger dataset.

    python engine.py bench_v1_sparse_run  --dirout ztmp/bench/   --topk 5


    """
    # create query df in ztmp directory
    dataset = "ag_news"
    collection_name = f"hf-{dataset}-sparse"
    dirtmp = f"{dirout}/{dataset}/df_search_test.parquet"

    if not os.path.exists(dirtmp):
        df = pd_read_file(f"{dirout}/norm/{dataset}/*/df_0.parquet")  ##  Real Dataset
        # pick thousand random rows
        df_query = df.sample(1000)
        pd_to_file(df_query, dirtmp)
    else:
        df_query = pd_read_file(dirtmp)

    model_id = "naver/efficient-splade-VI-BT-large-query"  ### 17 Mb
    model = EmbeddingModelSparse(model_id)

    cc = Box({})
    cc.metrics = []

    for i, row in df_query.iterrows():
        # print(row)
        id1 = row["id"]
        query = row["body"][:300]

        t0 = time.time()
        results = qdrant_sparse_search(
            query, collection_name=collection_name, model=model, topk=topk
        )
        dt = time.time() - t0
        top_5 = [scored_point.id for scored_point in results[:topk]]

        #### Accuracy.abs
        istop_k = 1 if id1 in top_5 else 0
        cc.metrics.append([id1, istop_k, dt])

    tunix = date_now(fmt="%Y%m%d_%H%M_%S", returnval="str")
    dirout2 = f"{dirout}/{dataset}/sparse/{tunix}/"
    dfmetrics = pd.DataFrame(cc.metrics, columns=["id", "istop_k", "dt"])
    pd_to_file(dfmetrics, f"{dirout2}/dfmetrics.csv", show=1)
    log(" Avg time per request", dfmetrics["dt"].mean())



###################################################################################################
if __name__ == "__main__":
    import fire
    # pd.options.mode.chained_assignment = None
    fire.Fire()



