cout_blocks = int(input())
blocks = {}
for _ in range(cout_blocks):
    wight, height = map(int, input().split())

    if wight in blocks and blocks[wight] < height:
        blocks[wight] = height
    elif wight not in blocks:
        blocks[wight] = height
        
print(sum(blocks.values()))
