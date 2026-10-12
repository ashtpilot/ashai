source ./venv/bin/activate
mlx_lm.lora \
    --model Qwen/Qwen3.5-4B-Base \
    --train \
    --data . \
    --iters 2000 \
    --steps-per-eval 200 \
    --batch-size 1 \
    --num-layers 4 \
    --max-seq-length 650 \
    --grad-checkpoint

mlx_lm.fuse --model Qwen/Qwen3.5-4B-Base --adapter-path ./adapters --save-path ./fused_model