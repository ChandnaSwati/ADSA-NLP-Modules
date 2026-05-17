"""
Verifier / Evaluator Agent
Goal: verify each generated claim against retrieved documents using
semantic similarity, NLI, and temporal checks.

Expected output → results/metrics.json
"""

# TODO: compute semantic similarity (Sentence-BERT cosine)
# TODO: use NLI model (BART-MNLI) for contradiction detection
# TODO: check temporal consistency (claim year vs doc year)
# TODO: aggregate metrics:
#        factual_precision, contradiction_rate, temporal_consistency, confidence
# TODO: return metrics dictionary

