#!/bin/bash

accelerate launch --multi_gpu --num_processes 2 training/finetune_ddp.py

