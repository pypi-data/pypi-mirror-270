"""The text module provides more general evaluation functions
for text generated by AI models."""

import sys

import dotenv

import lastmile_eval.text as lm_eval_text


def main():
    # Openai evaluators require openai API key in .env file.
    # See README.md for more information about `.env`.
    dotenv.load_dotenv()

    SUPPORTED_BACKING_LLMS = [
        "gpt-3.5-turbo",
        "gpt-4",
    ]

    print("Starting text evaluation examples.")

    for model_name in SUPPORTED_BACKING_LLMS:
        print(
            f"\n\n\n\nRunning example evaluators with backing LLM {model_name}"
        )
        text_scores_example_1(model_name)
        text_scores_example_2(model_name)
        text_scores_example_3(model_name)

    return 0


def text_scores_example_1(model_name: str):
    texts_to_evaluate = [
        "The quick brown fox jumps over the lazy dog.",
        "The quick brown fox jumps over the lazy dog.",
    ]
    references = [
        "The quick brown fox jumps over the lazy dog.",
        "The swift brown fox leaps over the lazy dog.",
    ]
    bleu = lm_eval_text.calculate_bleu_score(texts_to_evaluate, references)
    print("\n\nTexts to evaluate: ", texts_to_evaluate)
    print("References: ", references)
    print("\nBLEU scores: ", bleu)

    rouge1 = lm_eval_text.calculate_rouge1_score(texts_to_evaluate, references)
    print("\nROUGE1 scores: ", rouge1)

    exact_match = lm_eval_text.calculate_exact_match_score(
        texts_to_evaluate, references
    )

    print("\nExact match scores: ", exact_match)

    relevance = lm_eval_text.calculate_relevance_score(
        texts_to_evaluate, references, model_name=model_name
    )

    print("\nRelevance scores: ", relevance)

    summarization = lm_eval_text.calculate_summarization_score(
        texts_to_evaluate, references, model_name=model_name
    )

    print("\nSummarization scores: ", summarization)

    custom_semantic_similarity = (
        lm_eval_text.calculate_custom_llm_metric_example_semantic_similarity(
            texts_to_evaluate, references, model_name=model_name
        )
    )

    print("\nCustom semantic similarity scores: ", custom_semantic_similarity)


def text_scores_example_2(model_name: str):
    texts_to_evaluate = [
        "The quick brown fox jumps over the lazy dog.",
        "The quick brown fox jumps over the lazy dog.",
    ]
    references = [
        "The quick brown fox jumps over the lazy dog.",
        "The swift brown fox leaps over the lazy dog.",
    ]

    questions = ["What does the animal do", "Describe the fox"]

    qa = lm_eval_text.calculate_qa_score(
        texts_to_evaluate, references, questions, model_name=model_name
    )
    print("\n\nTexts to evaluate: ", texts_to_evaluate)
    print("References: ", references)
    print("\nQA scores: ", qa)

    human_vs_ai = lm_eval_text.calculate_human_vs_ai_score(
        texts_to_evaluate, references, questions, model_name=model_name
    )

    print("\nHuman vs AI scores: ", human_vs_ai)


def text_scores_example_3(model_name: str):
    texts_to_evaluate = [
        "I am happy",
        "I am sad",
    ]

    toxicity = lm_eval_text.calculate_toxicity_score(
        texts_to_evaluate, model_name=model_name
    )
    print("\nToxicity scores: ", toxicity)

    custom_sentiment = (
        lm_eval_text.calculate_custom_llm_metric_example_sentiment(
            texts_to_evaluate, model_name=model_name
        )
    )

    print("\nCustom sentiment scores: ", custom_sentiment)


if __name__ == "__main__":
    sys.exit(main())
