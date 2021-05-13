# boundary-layer-mycompany-plugin

This repo can be used as a template to customize your company's installation of boundary-layer. In fact, we do the same at Etsy.

## Setup
```
[boundary-layer-mycompany-plugin]> ll
total 40
drwxr-xr-x  11 vchiapaikeo  staff   352B May 12 22:21 .
drwxr-xr-x  44 vchiapaikeo  staff   1.4K May 12 22:02 ..
-rw-r--r--   1 vchiapaikeo  staff    97B May 12 22:05 .gitignore
-rw-r--r--   1 vchiapaikeo  staff   392B May 12 22:01 .pylintrc
-rw-r--r--   1 vchiapaikeo  staff    34B May 12 22:05 README.md
drwxr-xr-x   7 vchiapaikeo  staff   224B May 12 22:20 boundary_layer_mycompany_plugin
drwxr-xr-x   9 vchiapaikeo  staff   288B May 12 22:21 boundary_layer_mycompany_plugin.egg-info
-rw-r--r--   1 vchiapaikeo  staff    76B May 12 22:01 setup.cfg
-rw-r--r--   1 vchiapaikeo  staff   1.3K May 12 22:20 setup.py
drwxr-xr-x   3 vchiapaikeo  staff    96B May 12 22:13 test
[boundary-layer-mycompany-plugin]>
[boundary-layer-mycompany-plugin]> python3 -m venv venv
[boundary-layer-mycompany-plugin]>
[boundary-layer-mycompany-plugin]> pip install -e .[test]
Obtaining file:///Users/vchiapaikeo/development/boundary-layer-mycompany-plugin
Collecting boundary-layer<1.10,>=1.7.9 (from boundary-layer-mycompany-plugin==0.0.1)
  Using cached https://files.pythonhosted.org/packages/c6/94/70d40b09bc5d8e77c98cbaaa9aab3fe9bad146ff1a667f64ba5f66effd7d/boundary_layer-1.9.4-py2.py3-none-any.whl
Collecting pytest==3.2.3 (from boundary-layer-mycompany-plugin==0.0.1)
  Using cached https://files.pythonhosted.org/packages/8c/7d/f5d71f0e28af32388e07bd4ce0dbd2b3539693aadcae4403266173ec87fa/pytest-3.2.3-py2.py3-none-any.whl
Collecting jsonschema<3.0,>=2.6.0 (from boundary-layer<1.10,>=1.7.9->boundary-layer-mycompany-plugin==0.0.1)
  Using cached https://files.pythonhosted.org/packages/77/de/47e35a97b2b05c2fadbec67d44cfcdcd09b8086951b331d82de90d2912da/jsonschema-2.6.0-py2.py3-none-any.whl
Collecting semver<3.0,>=2.7.0 (from boundary-layer<1.10,>=1.7.9->boundary-layer-mycompany-plugin==0.0.1)
  Using cached https://files.pythonhosted.org/packages/0b/70/b84f9944a03964a88031ef6ac219b6c91e8ba2f373362329d8770ef36f02/semver-2.13.0-py2.py3-none-any.whl
Collecting six<2.0,>=1.11.0 (from boundary-layer<1.10,>=1.7.9->boundary-layer-mycompany-plugin==0.0.1)
  Using cached https://files.pythonhosted.org/packages/d9/5a/e7c31adbe875f2abbb91bd84cf2dc52d792b5a01506781dbcf25c91daf11/six-1.16.0-py2.py3-none-any.whl
Collecting marshmallow<3.0,>=2.13.6 (from boundary-layer<1.10,>=1.7.9->boundary-layer-mycompany-plugin==0.0.1)
  Using cached https://files.pythonhosted.org/packages/8d/5a/c8288b3fa34bfc5afeee56454db7c239b9d2f492c36172dafabf95c780af/marshmallow-2.21.0-py2.py3-none-any.whl
Collecting xmltodict<1.0,>=0.11.0 (from boundary-layer<1.10,>=1.7.9->boundary-layer-mycompany-plugin==0.0.1)
  Using cached https://files.pythonhosted.org/packages/28/fd/30d5c1d3ac29ce229f6bdc40bbc20b28f716e8b363140c26eff19122d8a5/xmltodict-0.12.0-py2.py3-none-any.whl
Collecting networkx<2.5,>=2.4 (from boundary-layer<1.10,>=1.7.9->boundary-layer-mycompany-plugin==0.0.1)
  Using cached https://files.pythonhosted.org/packages/41/8f/dd6a8e85946def36e4f2c69c84219af0fa5e832b018c970e92f2ad337e45/networkx-2.4-py3-none-any.whl
Collecting jinja2<3.0,>=2.8.1 (from boundary-layer<1.10,>=1.7.9->boundary-layer-mycompany-plugin==0.0.1)
  Using cached https://files.pythonhosted.org/packages/7e/c2/1eece8c95ddbc9b1aeb64f5783a9e07a286de42191b7204d67b7496ddf35/Jinja2-2.11.3-py2.py3-none-any.whl
Collecting pyyaml>=4.2b1 (from boundary-layer<1.10,>=1.7.9->boundary-layer-mycompany-plugin==0.0.1)
  Using cached https://files.pythonhosted.org/packages/ef/e9/d62912119552b157ed66dc8297ae6ac08629d7d5c497d4faa26b0c3a4efe/PyYAML-5.4.1-cp36-cp36m-macosx_10_9_x86_64.whl
Requirement already satisfied: setuptools in ./venv/lib/python3.6/site-packages (from pytest==3.2.3->boundary-layer-mycompany-plugin==0.0.1) (40.6.2)
Collecting py>=1.4.33 (from pytest==3.2.3->boundary-layer-mycompany-plugin==0.0.1)
  Using cached https://files.pythonhosted.org/packages/67/32/6fe01cfc3d1a27c92fdbcdfc3f67856da8cbadf0dd9f2e18055202b2dc62/py-1.10.0-py2.py3-none-any.whl
Collecting decorator>=4.3.0 (from networkx<2.5,>=2.4->boundary-layer<1.10,>=1.7.9->boundary-layer-mycompany-plugin==0.0.1)
  Using cached https://files.pythonhosted.org/packages/bc/b4/c208a551033a7abb67703be73dea3d917dbce528bd87bcd6f7dfceec7097/decorator-5.0.7-py3-none-any.whl
Collecting MarkupSafe>=0.23 (from jinja2<3.0,>=2.8.1->boundary-layer<1.10,>=1.7.9->boundary-layer-mycompany-plugin==0.0.1)
  Using cached https://files.pythonhosted.org/packages/2f/73/2f1acfb49f2304b550ab7932e3102b7997b1beef03458ec7bd25f7f60608/MarkupSafe-2.0.0-cp36-cp36m-macosx_10_9_x86_64.whl
Installing collected packages: jsonschema, semver, six, marshmallow, xmltodict, decorator, networkx, MarkupSafe, jinja2, pyyaml, boundary-layer, py, pytest, boundary-layer-mycompany-plugin
  Running setup.py develop for boundary-layer-mycompany-plugin
Successfully installed MarkupSafe-2.0.0 boundary-layer-1.9.4 boundary-layer-mycompany-plugin decorator-5.0.7 jinja2-2.11.3 jsonschema-2.6.0 marshmallow-2.21.0 networkx-2.4 py-1.10.0 pytest-3.2.3 pyyaml-5.4.1 semver-2.13.0 six-1.16.0 xmltodict-0.12.0
You are using pip version 18.1, however version 21.1.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
[boundary-layer-mycompany-plugin]>
```

## Build DAG

```
[boundary-layer-mycompany-plugin]> boundary-layer build-dag test/data/test_dag.yaml
2021-05-12 22:22:45,850 - boundary-layer v. 1.9.4 - INFO - Loaded plugins default, mycompany
# -*- coding: utf-8 -*-
#
# This file was auto-generated at 2021-05-13T02:22:45.873771 by boundary-layer, version 1.9.4.
#
#                           DO NOT EDIT!
#
# The configuration that generated this DAG was:
#   filename: /Users/vchiapaikeo/development/boundary-layer-mycompany-plugin/test/data/test_dag.yaml
#       date: 2021-05-13T02:22:45.873771
#        md5: 73446034491253041faa16b440bf2c0c
#
# The configuration contents are below:
###############################################################################
# name: my_test_dag
#
# dag_args:
#   concurrency: 2
#   max_active_runs: 1
#   schedule_interval: '@daily'
#   catchup: true
#
# default_task_args:
#   owner: vchiapaikeo
#   retries: 1
#   retry_delay: 1
#   start_date: '2021-05-01'
#   depends_on_past: false
#
# operators:
# - name: parent_task
#   type: bash
#   properties:
#     bash_command: "sleep 10"
#
# - name: another_parent_task
#   type: bash
#   upstream_dependencies:
#     - parent_task
#   properties:
#     bash_command: "sleep 10"
#
# - name: new_task
#   type: gcp_cloud_function_invoke
#   upstream_dependencies:
#     - another_parent_task
#   properties:
#     function_id: my-function-name
#     input_data:
#       bucket: mybucket
#       path: path/to/data/parquet/
#     location: us-west1
#
###############################################################################
#

import os
import re
from airflow import DAG

import datetime

from airflow.operators.bash_operator import BashOperator
from airflow.providers.google.cloud.operators.functions import CloudFunctionInvokeFunctionOperator

DEFAULT_TASK_ARGS = {
        'owner': 'vchiapaikeo',
        'retries': 1,
        'retry_delay': 1,
        'start_date': '2021-05-01',
        'depends_on_past': False,
    }

dag = DAG(
        schedule_interval = '@daily',
        concurrency = 2,
        catchup = True,
        max_active_runs = 1,
        dag_id = 'my_test_dag',
        default_args = DEFAULT_TASK_ARGS,
    )

parent_task = BashOperator(
        dag = (dag),
        start_date = (datetime.datetime(2021, 5, 1, 0, 0)),
        task_id = 'parent_task',
        bash_command = 'sleep 10',
        retry_delay = (datetime.timedelta(0, 1)),
    )


another_parent_task = BashOperator(
        dag = (dag),
        start_date = (datetime.datetime(2021, 5, 1, 0, 0)),
        task_id = 'another_parent_task',
        bash_command = 'sleep 10',
        retry_delay = (datetime.timedelta(0, 1)),
    )

another_parent_task.set_upstream(parent_task)

new_task = CloudFunctionInvokeFunctionOperator(
        dag = (dag),
        start_date = (datetime.datetime(2021, 5, 1, 0, 0)),
        input_data = { 'bucket': 'mybucket','path': 'path/to/data/parquet/' },
        task_id = 'new_task',
        retry_delay = (datetime.timedelta(0, 1)),
        function_id = 'my-function-name',
        location = 'us-west1',
    )

new_task.set_upstream(another_parent_task)
```
