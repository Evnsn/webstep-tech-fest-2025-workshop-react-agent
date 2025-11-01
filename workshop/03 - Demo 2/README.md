# Demo 2
## No ReAct loop:
**Input prompt**
```
What is (2(3+4*5)+3)/7?
```

## No system prompt
**Input prompt**
```
What is (2(3+4*5)+3)/7?
```

## Correct!
**System prompt:**
```
Use the following format iteratively:
===
**REASON:** [VERY specific description of your next step]
**ACTION:** [What function with what parameter you will call]
===

Once you have the answer, use this format:
===
**FINAL:** [Your final answere]
===

IMPORTANT
- In your *REASON* step, use substitution, e.g A=3+4, B=A-2
```

**Input prompt**
```
What is (2(3+4*5)+3)/7?
```