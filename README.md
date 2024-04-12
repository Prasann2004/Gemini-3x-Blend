# Gemini-3x-Blend
I implemented the following techniques to improve the output from Gemini :
## [Corrective-Retrieval-Augmented-Generation](https://arxiv.org/abs/2401.15884) .
![image](https://github.com/Prasann2004/Corrective-Retrieval-Augmented-Generation-Implementation/assets/83667133/e894c778-cf01-4e94-888c-1a7b3ea102ca)
Corrective Retrieval Augmented Generation integrates a lightweight retrieval evaluator designed to assess the quality of retrieved documents in relation to a given query. This evaluator provides a confidence score that informs subsequent retrieval actions, allowing for adaptive adjustments in knowledge retrieval strategies. Importantly, CRAG extends beyond static and limited corpora by leveraging large-scale web searches to augment retrieval results, thereby expanding the breadth and depth of available information.

Algorithm : 

1. Require :E (Retrieval Evaluator), W (Query Rewriter), G (Generator)

2. Input :x (Input question), D = {d1, d2, ..., dk} (Retrieved documents)

3. Output :y (Generated response)

4. scorei = evaluates the relevance of each pair (x, di), di ∈ D

5. Confidence = Calculate and give a final judgment based on {score1, score2,...scorek}

// Confidence has 3 optional values: [CORRECT], [INCORRECT] or [AMBIGUOUS]

6. if Confidence == [CORRECT] then

       Internal_Knowledge = Knowledge_Refine(x, D)
    
        k = Internal_Knowledge
    
7. else if Confidence == [INCORRECT] then

        External_Knowledge = Web_Search(W Rewrites x for searching)
    
        k = External_Knowledge
    
8. else if Confidence == [AMBIGUOUS] then

        Internal_Knowledge = Knowledge_Refine(x, D)
    
        External_Knowledge = Web_Search(W Rewrites x for searching)
    
        k = Internal_Knowledge + External_Knowledge
    
9. end
    
       G predicts y given x and k
## [LLM-Blender-Implementation](https://arxiv.org/abs/2306.02561)
![Document -- SmartDraw - Google Chrome 12-04-2024 11_44_06](https://github.com/Prasann2004/Gemini-3x-Blend/assets/83667133/827fb8ee-b9ba-489b-bc1c-c2f54fa29569)

LLM-Blender is a novel framework designed to enhance the performance of large language models (LLMs) by combining the strengths of multiple models. It consists of two key modules: **PairRanker** and **GenFuser**. PairRanker utilizes a specialized method for pairwise comparison of candidate outputs, leveraging cross-attention encoders to determine the superior one based on input text. Results show that PairRanker correlates highly with ChatGPT-based ranking. GenFuser merges the top-ranked candidates to generate an improved output by capitalizing on their strengths and addressing weaknesses. The framework is evaluated using a benchmark dataset called MixInstruct, showcasing significant performance improvements over individual LLMs and baseline methods across various metrics.


## [SELF-DISCOVER: Large Language Models Self-Compose Reasoning Structures](https://arxiv.org/abs/2402.03620)
 ![(794) Build SELF-DISCOVER from Scratch with LlamaIndex - YouTube - Google Chrome 03-03-2024 23_18_20](https://github.com/Prasann2004/SELF-DISCOVER-Implementation/assets/83667133/c12aa649-99b9-4fde-879a-1dbcd7ec3fe4)

