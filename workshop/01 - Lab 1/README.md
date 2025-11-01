# Problems
## 1. Make Agent return structured output.
### Example 1:  
**Input:**
```
“My name is Adrian, I’m 30.”
```

**Output:**  
```json
{
    “name”: “Adrian”,
     “age”: 30
}
```

### Example 2:
**System prompt:**
```
Please return JSON-formatted list. I want the fields per element; "ingredients", "amount", "unit", and "recipe".
```

**User input:**
```
Ingredienser
KJØTTKAKER
600 g kjøttdeig
1/4 ts nykvernet sort pepper (smak til)
3 ss potetmel
2 ss løk , finhakket (kan sløyfes)
1 1/2 ts salt (smak til)
2 dl melk eller vann (ca.)
BRUN SAUS
40 g smør
35 g hvetemel (ca.)
5 dl kjøttkraft (eller utblandet buljong/fond*), varm
soyasaus (smak til)
salt og nykvernet sort pepper
KÅLSTUING
500 g hodekål (ca.)
30 g smør
30 g hvetemel (ca.)
3 1/2 dl melk , varm (ca.)
muskatnøtt , revet (smak til)
salt og eventuelt litt (hvit) pepper
TILBEHØR
4 porsjoner poteter
4 gulrøtter
tyttebærsyltetøy
```

Make Agent count from 0 to X one number at the time. X is given by user.
Make Agent count from 0 to X using tool: add(). 

## 2. 


Make Agent call multiple tools (turn on ALL tools)
Example: “What is 5+4-3*2/1”
Example: “How many work at each location at Webstep?”





## 1. Make the Agent count itteratively from 0 to a given number by the user - using system prompth.
Demonstration
```

```

User input:
```
3
```

## 2. Make the Agent count itteratively from 0 to a given number by the user - using system prompth + tool call `add()`.
...

## 3. Make the Agent use multiple tools
...

### User input
#### 1. Calculation:
```
5-4*3/2+1
```

#### 2. Fetch weather
```
What's the weather at all our locations?
```

## Bonus: Make the longest consequent text using system prompth and temperature.
### User input
```
Hva er Webstep?
```

## Bonus: Make a pirat-encrypting-agent - without tools
**Description:** Given a word or a sentence, transforming by doubling every consonant and placing an ‘o’ in between.  
### User inputs
```
Webstep
```

### Solution
```
Wowebobsostotepop
```


