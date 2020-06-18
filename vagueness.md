# Ideas on Vagueness 

## Background
- vagueness is important 
    - sorites paradox: not just a thought experiment 
    - most non-mathematical predicates are vague 
    - how are we going to reach language understanding without some concept of vagueness 
- theories/approaches to vagueness 
    - fuzzy logic (forget that shit) 
    - epistemicism: the line exists but we don't know where 
    - contextualism: the line exists but keeps moving as we zoom in 
    - Graff: sort of contextual, dependent on similarity etc
    - Shapiro: also dependent on common ground 
- if reader is with me so far: we have accepted that 
    a. vague predicates are common in language and 
    b. the extension of vague predicates is likely dependent on various linguistic factors including the speaker, context, and discourse
- extension vs meaning 
    - forget meaning, nobody knows what it is
    - extension: set of things to which that applies 
    - that's much closer to what we are trying to learn with ML
    - a model that generalizes to unseen data can tell you whether something is in the extension or not (set builder notation style) 

## Vagueness in NLP 
- let's shift gears to NLP 
    - those vague predicates haven't gone away
    - consider examples from: SuperGLUE, other benchmarks 
    - 2 problems
        1. non-contextual, no speaker info 
        2. treating extension of vague predicates as non-vague 
    - (1) lies out of scope. All of NLP should strive for 1, but we're dealing with a model here so let's leave that aside for a minute 
    - (2) is a problem with the data and the way we approach the notion of truth 
- why is (2) a problem
    - at the end of the day, we want to capture something "true" (whatever that means) 
    - without question, you can fit an NN to any data and capture the most arbitrary of correlations 
    - but if in fact our goal is to capture something true by training models on data,  we ensure that that 
        i. our data is capturing something real (probably the case) 
        ii. our data is capturing that at the correct granularity   
    - both are of concern
    - if we have a vague predicate labeled categorically, then we could violate both 
        - obviously if we are trying to capture extension and we are not labeling our data correctly, then we won't capture the full extension
        - but also depending on our theory of vagueness, we are in fact allowing mistakes to be entered as "true" 

- in labeling things as we are, we are imposing a view of vagueness that is almost certainly wrong 
    - there are a lot of theories of vagueness but none of them pretend that vagueness doesn't exist 
    - the "ostrich" theory of vagueness 

## Concrete approach to solve that 
- use a decomp-style sliding bar approach 
- stop using forced-choice annotation 
    - let the people speak 
    - language isn't what you want it to be or what's easy to label 
    - it's how people use language 
    - since we don't know what meaning of predicates, let's give annotators a bit more freedom in choosing the meaning 

## Concrete example: analytic truth 
- Let's take something that, if anything admits of a categorical labeling scheme, should 
- analytic truth
- if you wanna live 100 years in the past so fuckin bad, here you go
- analytic statements are either true or false, right? 
- fuckin WRONG
- here's the distribution from actual annotators on that
- and here's what happens when you train models under that categorical assumption  
- do I need to train a model on the other data? 

## other thoughts
- let's look at those "human performance" numbers in GLUE
- can I get my hands on the actual predictions by humans? 
- if so, can we look at what humans "get wrong" and say that this is because of vague predicates 

