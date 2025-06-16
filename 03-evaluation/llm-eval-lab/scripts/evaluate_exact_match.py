with open("reference_outputs/references.txt") as ref_file, open("generated_outputs/generations.txt") as gen_file:
    references = [line.strip() for line in ref_file]
    generations = [line.strip() for line in gen_file]

exact_matches = sum([r == g for r, g in zip(references, generations)])
accuracy = exact_matches / len(references)

print(f"Exact Match Accuracy: {accuracy*100:.2f}%")

