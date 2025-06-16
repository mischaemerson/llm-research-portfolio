#!/bin/bash

# Adjust these paths if needed
LOCAL_BUILD_PATH=~/llm-research-portfolio
GITHUB_REPO_PATH=~/llm-research-portfolio

# Copy full project phase directories into GitHub repo directory
for PHASE in 01-fine-tuning 02-data-cleaning 03-evaluation 04-responsible-ai 05-distributed-training 06-inference-serving 07-rlhf 08-cot-prompting
do
  echo "Syncing phase: $PHASE"
  rsync -av --delete $LOCAL_BUILD_PATH/$PHASE/ $GITHUB_REPO_PATH/$PHASE/
done

echo "Sync completed successfully!"
