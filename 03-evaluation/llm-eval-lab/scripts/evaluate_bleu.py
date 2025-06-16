import sacrebleu

with open("reference_outputs/references.txt") as ref_file, open("generated_outputs/generations.txt") as gen_file:
    references = [line.strip() for line in ref_file]
    generations = [line.strip() for line in gen_file]

bleu = sacrebleu.corpus_bleu(generations, [references])
print(f"BLEU score: {bleu.score:.2f}")

