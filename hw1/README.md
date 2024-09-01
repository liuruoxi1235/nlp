1.4
Question 1:

the president ate a president ! 

every sandwich kissed a chief of staff .

the sandwich on the delicious president in the pickle pickled a fine fine chief of staff !

a pickle pickled a floor !

is it true that every pickle wanted every pickle ?

the pickle kissed the floor in every chief of staff with the perplexed pickle .

a chief of staff in every president with a president with a president with the president with a pickle on a president with every sandwich kissed a sandwich .

is it true that a chief of staff ate the president in every sandwich with the chief of staff in the president on the sandwich on every delicious fine floor under the chief of staff with a fine pickle with a chief of staff in a president in the sandwich under the floor with a president on every pickled president under the fine delicious chief of staff in the floor on a president in a pickle ?

a chief of staff in every president with a president with a president with the president with a pickle on a president with every sandwich kissed a sandwich .

is it true that the floor understood every pickled pickle on the floor in every sandwich under the chief of staff with the perplexed sandwich with every floor on every fine pickle in the pickled president in every sandwich with the floor under a pickle with a floor with the chief of staff with the sandwich with a president ?

Question 2:
(ROOT (S (NP (Det every)
             (Noun sandwich))
         (VP (Verb pickled)
             (NP (NP (Det every)
                     (Noun chief
                           of
                           staff))
                 (PP (Prep with)
                     (NP (Det the)
                         (Noun sandwich))))))
      .)


(ROOT (S (NP (NP (NP (NP (NP (Det a)
                             (Noun floor))
                         (PP (Prep under)
                             (NP (Det the)
                                 (Noun president))))
                     (PP (Prep with)
                         (NP (NP (Det the)
                                 (Noun pickle))
                             (PP (Prep in)
                                 (NP (Det a)
                                     (Noun floor))))))
                 (PP (Prep on)
                     (NP (Det the)
                         (Noun pickle))))
             (PP (Prep on)
                 (NP (Det every)
                     (Noun pickle))))
         (VP (Verb ate)
             (NP (Det the)
                 (Noun chief
                       of
                       staff))))
      !)

Question 3:
(ROOT (S (NP (Det the)
             (Noun sandwich))
         (VP ...
             ...))
      ...)

(ROOT (S (NP (NP (Det every)
                 (Noun ...))
             ...)
         ...)
      ...)

2.1 
Question 1
The mainly responsible grammar rule for long sentences is NP -- NP PP. As this grammar rule make recursive definition of NP: if this rule is choose for new NP in previous NP, the pattern will repeat util finally the other rule of NP (NP, Det, Noun) is chosen at some part. Also, as the only rule for PP is Prep and NP, it will generate another NP in the sequence. As a result, the average expactation of NPs in the expansion of a NP is (2+0)/2 = 1, meaning whenever an NP is expanded, it is expected to generate another NP in its expanded sequence. This is likely to cause the sentence to be very long, as NP pattern can extend unlimitedly.

Question 2
For Noun, the possible rules in current grammar are: (Noun -- adj, Noun) and (Noun -- [terminator]), where there are five possible choices of terminator. Since the weight for any of the terminators is the same as the weight for (Noun -- adj, Noun), the chance of adding an adj before the noun at any noun expansion step is only 1/6, and having consecutive adjectives, , as in example "the fine perplexed pickle", means choosing two adj & Noun rule consecutively. The chance is only 1/36. 

Question 3
To fixed item 1 we should make the weight for NP NP PP rule smaller, so that the expectation for another NP in the expansion of a NP is smaller; to fix item 2 we should make the weight for (Noun -- Adj Noun) rule larger to make it more likely to yield consecutive adjectives.

Question 4
Not yet solved

Question 5
a sandwich ate the delicious president ! 

a fine delicious pickle pickled the floor . 

every sandwich understood the chief of staff .

a chief of staff with every perplexed floor with the sandwich wanted the perplexed floor .

a chief of staff pickled a delicious sandwich !

every fine pickled sandwich ate a pickle under a perplexed president in the floor !

the pickle ate a floor under every chief of staff .

the delicious president on every floor in a pickle on a delicious pickle ate every pickle .

the pickled delicious pickled floor kissed a sandwich .

the pickled pickled chief of staff ate the floor .

2.3
Question 9:
Modifications:
sentence 1: 
NP Name
Name Sally
This is to ensure that NP can be formed with either an normal Noun with an article or just a name (article is not needed). As name is a special kind of noun, a different category need to be established.

sentence 2:
Verb  Verb Con Verb
NP    NP   Con NP 
Con   and
This is to make that NP can be formed with two NP combining together with "and" and two transitive verbs can be combined together to be the verb for the whole sentence

sentence 3:
VP IVP
IVP Intrans
Intrans sighed
Intrans worked
We created IVP to represent to phrase begin with an intransitive verb. In the case of sentence 3, the IVP is only consist of an intransitive verb.

sentence 4:
S  NP Verb_sentece SS
Verb_sentence thought
SS that NP VP
We created a type called SS (stands for sub sentence that is consist of that, NP and VP). In this case, the whole sentence will serve as a Noun in the sentence. For sentences like sentence 4, a transitive verb is needed and followed by a sub sentence. However, the verb here is different from normal transitive verb: for verbs like thought, its unreasonable to have "I thought Sally", but reasonable for "I thought that (a sentence)". This kind of verb can only get followed by a sentence, and we decide to have a different type of verb for that.

sentence 5:
S it AV NP SS
AV perplexed
For sentences like sentence 5, we found that the verb is a different type: it is a adjective but act as a verb in the sentence (it perplexed Michael = it makes Michael perplexed). This type of verb is special and need a distinctive type. Then, the sentence is consist of it, AV, NP and a substance.

sentence 6:
S SS AV NP
Sentences like sentence 6 are similar to sentence 5 but just different in the order of the components: for sentence 6 it put the sub sentence at the beginning and does not need "it" at the beginning.

sentence 7:
Adj Adv Adj
Adv very
Sentences like sentence 7 introduce adverb that can be used to describe adjective. This type of word need a different category and Ajd can be formed with an ad verb and an adj

sentence 8
IVP Intrans PP
Even though intransitive verb cannot be followed by a noun, it can be followed by a proposition (for instance, sighed in the room). Sentences like sentence 8 just show this pattern: a phrase start with intransitive verb can be consist of an intransitive verb and a proposition phrase.

Question 10:
every pickled pickle worked in every pickled delicious president !

is it true that it perplexed every pickled pickle that every pickle and every chief of staff sighed on every pickle ? 

Sally ate that every floor pickled every very pickled chief of staff .

that every pickled president sighed in a sandwich perplexed the very pickled perplexed chief of staff !

is it true that a sandwich sighed ?

is it true that the very pickled president with a floor with the very perplexed sandwich and the pickle on every sandwich under a pickle kissed every delicious sandwich on Sally and every sandwich ?

it perplexed every sandwich that the president thought every sandwich !

the pickle wanted and understood that every sandwich sighed with Sally .

Sally wanted that Sally worked .

it perplexed Sally that Sally worked with every delicious chief of staff !

2.4 

Neural hardware implementation of tree-structured language behaviors
It's somehow impossible for neural networks to have a concept like noun phrase or verb phrase (definitely neural network don't have mind, just mean that they do not use these concepts to form natural langauge outputs). However, the grammar will represent some patterns of words' combinations (for example, they often found proposition after a noun, while never a noun after an intransitive verb), and can definitely learn these patterns in the process of traning. Also, as sequencial data processing neural networks (like LSTM) and Multi-head attention mechanism of Transformmers allow neural network to "memorize" and refer t long previous context when formming outputs, also allowing neural networks to learn "longer" grammar patterns (for instance, NP VP sentence structure can have a very long NP)

Possibilities of understanding unnatural languages
It might be possible for neural networks to learn such languages: they are learning through combinations of different word patterns, and the grammar is just a higher level rule governing those word patterns. It's more like an abstract concept that guides natural language, while neural networks are learning through lower level word patterns. For unnatural languages, as long as their word formation have patterns (if there isn't pattern for words sequence, then the language should be similar to nonsense), neural networks will be able to learn such pattern. For human babies, they learn language in a similar way with neural network: instead of learning grammar first, they learn the langauge through mimicing their parents' pronunciation in the beginning, and then learning from the sentences and articles they read. For unnatural languages, they can still learn in this way. Whether the langauge have a grammar or not is not that important. For native speakers of a langauge, they usually does not have a clear concept about grammar, while still able to write grammarly correct sentences. Grammar is more abstract than the actual way for neural network and human infants to learn language. 

Why is tree-structured language used and evolved
This is perhaps a iterative process: perhaps at the beginning natural langauges are quite different from their current version: their might be different grammars (or not as big as grammar, just some conventions for formming language) for different people: People create these grammars because they need to convey information, and having some general rules match their thinking pattern (when coming up with information, people will definitely have some pattern). In the process of communication, those slightly different version of grammars gradually merge together into a universal rules governing the language. The best way to convey information in a language definitely does not exist: in some languages verb is at the beginning, while in other languages verb is at the end. If there is a universally best sequence of sentence components for information exchange, such difference among natural languages won't exist, also suggesting that developing grammar patterns is a distinctive process for each kind of natural langauge.

Grammar's modeling of langauge
Grammar is a high-level characteristic of language. It's hard to say whether ungrammarical sentences will affect people's understanding of the language. For our observation, if there is some grammar errors like "Sally eat an apple", it will not affect people's understanding, while other more significant errors like putting verb at the end of the sentence may make sentences confusing. As grammar is a convention followed by nearly all speakers and writers of natural languages, it is an acceptable way to model language. However, creating a universal grammar might be hard: in the bottom level, grammars are just norms when people speak and write, and it's hard to attribute each low-level pattern to a high-level abstract rule. If people try to do so, it might results in a huge grammar rule repository (actually when we try to create some perfect sentence generators for 2.2, we end up having a really ugly grammar rule set, and we decide to remove a lot of this rules). The way we use for 2.2 is perhaps a solution: grammar rules make sure that big parts of sentences follows the grammar norm, while for smaller part of sentence like specific word choice human's own choice and convention might be more evident (grammars should not differentiate between nouns that can or cannot eat things, but speakers and writers should). In this way, grammar rules will not overkill while still provide effective guidance.

3.3
Question 2
Original sentence and structure:
(ROOT (S (NP (Name Sally))
         (VP (IVP (Intrans worked)
                  (PP (Prep with)
                      (NP (NP (NP (NP (Det every)
                                      (Noun sandwich))
                                  (Con and)
                                  (NP (Det the)
                                      (Noun president)))
                              (PP (Prep in)
                                  (NP (Det a)
                                      (Noun desk))))
                          (PP (Prep under)
                              (NP (Det the)
                                  (Noun desk))))))))
      .)

Structure parser produced:
(ROOT (S (NP (Name Sally))
         (VP (IVP (Intrans worked)
                  (PP (Prep with)
                      (NP (NP (Det every)
                              (Noun sandwich))
                          (Con and)
                          (NP (NP (Det the)
                                  (Noun president))
                              (PP (Prep in)
                                  (NP (NP (Det a)
                                          (Noun desk))
                                      (PP (Prep under)
                                          (NP (Det the)
                                              (Noun desk)))))))))))
      .)

Full sentence: Sally worked with every sandwich and the president in a desk under the desk

In this example, the phrase that each proposition phrase describe is different in the original structure generated by randsent.py and the one parsed by parse program. For the original one, "in a desk" is describing both sandwich and the president, indicating that Sarah is working with sandwich (in a desk) and the president (in a desk), and the final proposition phrase "under the desk" is describing the whole phrase "every sandwich and the president in a desk". In the parser version, "in a desk" is only describing the president, and "under the desk" is only describing the desk. The sentence means that Sally worked with every sandwich and the president (the president is in a desk (the desk is under the desk)). Two version have different meanings. Since the sentence itself is not that logical, we cannot analyze which one is closer to human convention.

Original sentence and structure:
(ROOT (S (NP (NP (NP (NP (Det every)
                         (Noun desk))
                     (PP (Prep in)
                         (NP (Det every)
                             (Noun (Adj (Adv very)
                                        (Adj (Adv very)
                                             (Adj (Adv very)
                                                  (Adj pickled))))
                                   (Noun chief
                                         of
                                         staff)))))
                 (PP (Prep with)
                     (NP (Name Sally))))
             (PP (Prep under)
                 (NP (Det a)
                     (Noun proposal))))
         (Verb_sentence thought)
         (SS that
             (NP (Det a)
                 (Noun pickle))
             (VP (IVP (Intrans sighed)
                      (PP (Prep under)
                          (NP (Det a)
                              (Noun chief
                                    of
                                    staff)))))))
      !)

Structure parser produced:
(ROOT (S (NP (NP (Det every)
                 (Noun desk))
             (PP (Prep in)
                 (NP (NP (Det every)
                         (Noun (Adj (Adv very)
                                    (Adj (Adv very)
                                         (Adj (Adv very)
                                              (Adj pickled))))
                               (Noun chief
                                     of
                                     staff)))
                     (PP (Prep with)
                         (NP (NP (Name Sally))
                             (PP (Prep under)
                                 (NP (Det a)
                                     (Noun proposal))))))))
         (Verb_sentence thought)
         (SS that
             (NP (Det a)
                 (Noun pickle))
             (VP (IVP (Intrans sighed)
                      (PP (Prep under)
                          (NP (Det a)
                              (Noun chief
                                    of
                                    staff)))))))
      !)
Full sentence: every desk in every very very very pickled chief of staff with Sally under a proposal thought that a pickle sighed under a chief of staff !

In the structure produced by randsent.py, the two proposition phrase, "with Sally" and "under a proposal" are both describing "every desk in every very very very pickled chief of staff", while in the structure produced by the parser, "with Sally" is still describing the desk while "under a proposal" is describing Sally. Two sentence have different meanings.

From the example, we can discover that when the parser program parse sentence with proximity principle: the proposition phrase is always used to describe the closest noun, while randsent may produce some structure with proposition phrase describing some far noun.

Question 3

There are 5 derivations

Derivation 1: "with a pickle", "on the floor", "under the chief of staff" are all describing the sandwich. The meaning of the noun is every sandwich with the properties: with a pickle, on the floor, under the chief of staff.
(NP (NP (NP (NP (Det every)
                (Noun sandwich)))
            (PP (Prep with)
                (NP (Det a)
                    (Noun pickle)))
        (PP (Prep on)
            (NP (Det the)
                (Noun) floor))
    (PP (Prep under)
        (NP (Det the)
            (Noun chief
                  of
                  staff)))))

Derivation 2: "with a pickle" is describing sandwich, and "on the floor" and "under the chief of staff" are both describing the pickle. The phrase means every sandwitch with a pickle that is on the floor and under the chief of staff.
(NP (NP (Det every)
        (Noun sandwich))
    (PP (Prep with)
        (NP (NP (Det a)
                (Noun pickle)))
            (PP (Prep on)
                (NP (Det the)
                    (Noun) floor))
        (PP (Prep under)
            (NP (Det the)
                (Noun chief
                      of
                      staff)))))

Derivation 3: "with a pickle" in describing sandwich, "on the floor" is describing pickle, and "under the chief of staff" is describing the floor. The phrase means every sandwich with a pickle that is on the floor (the floor is under the chief of staff)
(NP (NP (Det every)
        (Noun sandwich))
    (PP (Prep with)
        (NP (Det a)
            (Noun pickle))
        (PP (Prep on)
            (NP (Det the)
                (Noun) floor))
            (PP (Prep under)
                (NP (Det the)
                    (Noun chief
                            of
                            staff)))))

sandwich pickle floor chief of staff
1 floor sandwich chief of staff sandwich
2 floor pickle chief of staff pickle
3 floor pickle chief of staff floor
4 floor pickle chief of staff sandwich

Derivation 4: "with a pickle" is describing sandwich, "on the floor" is describing pickle, and "under the chief of staff" is also describing the sandwich. The phrase means sandwich with a pickle (the pickle is on the floor) and under the chief of staff.

(NP (NP (NP (Det every)
            (Noun sandwich))
        (PP (Prep with)
            (NP (Det a)
                (Noun pickle))
            (PP (Prep on)
                (NP (Det the)
                    (Noun) floor))
    (PP (Prep under)
        (NP (Det the)
            (Noun chief
                  of
                  staff))))))

Derivation 5: "with a pickle" and "on the floor" are both describing sandwich, while "under the chief of staff" is describing the floor. The phrase means sandwich with a pickle and on the floor (the floor is under the chief of staff)

(NP (NP (NP (Det every)
            (Noun sandwich))
        (PP (Prep with)
            (NP (Det a)
                (Noun pickle))
    (PP (Prep on)
        (NP (Det the)
            (Noun) floor))
        (PP (Prep under)
            (NP (Det the)
                (Noun chief
                    of
                    staff))))))

Question 4
Example outputs of grammar.gr:

Example 1: (ROOT (S (NP (NP (NP (Det the)
                     (Noun (Adj pickled)
                           (Noun pickle)))
                 (PP (Prep in)
                     (NP (NP (Det the)
                             (Noun president))
                         (PP (Prep under)
                             (NP (NP (Det the)
                                     (Noun president))
                                 (PP (Prep with)
                                     (NP (NP (Det a)
                                             (Noun president))
                                         (PP (Prep with)
                                             (NP (NP (NP (NP (NP (Det a)
                                                                 (Noun pickle))
                                                             (PP (Prep in)
                                                                 (NP (Det the)
                                                                     (Noun pickle))))
                                                         (PP (Prep in)
                                                             (NP (NP (Det every)
                                                                     (Noun floor))
                                                                 (PP (Prep under)
                                                                     (NP (Det the)
                                                                         (Noun sandwich))))))
                                                     (PP (Prep under)
                                                         (NP (Det the)
                                                             (Noun floor))))
                                                 (PP (Prep on)
                                                     (NP (Det a)
                                                         (Noun floor))))))))))))
             (PP (Prep in)
                 (NP (NP (Det the)
                         (Noun floor))
                     (PP (Prep with)
                         (NP (NP (Det every)
                                 (Noun chief
                                       of
                                       staff))
                             (PP (Prep in)
                                 (NP (NP (Det every)
                                         (Noun pickle))
                                     (PP (Prep under)
                                         (NP (NP (Det every)
                                                 (Noun (Adj pickled)
                                                       (Noun president)))
                                             (PP (Prep on)
                                                 (NP (NP (Det a)
                                                         (Noun sandwich))
                                                     (PP (Prep in)
                                                         (NP (NP (Det the)
                                                                 (Noun (Adj perplexed)
                                                                       (Noun pickle)))
                                                             (PP (Prep on)
                                                                 (NP (NP (Det a)
                                                                         (Noun floor))
                                                                     (PP (Prep in)
                                                                         (NP (Det the)
                                                                             (Noun (Adj fine)
                                                                                   (Noun (Adj perplexed)
                                                                                         (Noun (Adj delicious)
                                                                                               (Noun pickle)))))))))))))))))))))
         (VP (Verb wanted)
             (NP (NP (Det a)
                     (Noun floor))
                 (PP (Prep in)
                     (NP (NP (Det every)
                             (Noun chief
                                   of
                                   staff))
                         (PP (Prep with)
                             (NP (NP (Det a)
                                     (Noun sandwich))
                                 (PP (Prep on)
                                     (NP (NP (Det the)
                                             (Noun pickle))
                                         (PP (Prep in)
                                             (NP (NP (Det a)
                                                     (Noun sandwich))
                                                 (PP (Prep under)
                                                     (NP (NP (NP (NP (Det every)
                                                                     (Noun chief
                                                                           of
                                                                           staff))
                                                                 (PP (Prep with)
                                                                     (NP (Det a)
                                                                         (Noun chief
                                                                               of
                                                                               staff))))
                                                             (PP (Prep on)
                                                                 (NP (Det every)
                                                                     (Noun (Adj delicious)
                                                                           (Noun floor)))))
                                                         (PP (Prep under)
                                                             (NP (Det every)
                                                                 (Noun chief
                                                                       of
                                                                       staff))))))))))))))))
      .)
# number of parses = 185392049700

Example 2:
(ROOT (S (NP (NP (Det every)
                 (Noun sandwich))
             (PP (Prep on)
                 (NP (NP (NP (NP (Det every)
                                 (Noun pickle))
                             (PP (Prep in)
                                 (NP (Det every)
                                     (Noun sandwich))))
                         (PP (Prep under)
                             (NP (Det the)
                                 (Noun (Adj pickled)
                                       (Noun sandwich)))))
                     (PP (Prep in)
                         (NP (Det the)
                             (Noun president))))))
         (VP (Verb understood)
             (NP (NP (Det every)
                     (Noun (Adj fine)
                           (Noun chief
                                 of
                                 staff)))
                 (PP (Prep under)
                     (NP (NP (NP (NP (Det every)
                                     (Noun floor))
                                 (PP (Prep on)
                                     (NP (Det every)
                                         (Noun pickle))))
                             (PP (Prep with)
                                 (NP (Det a)
                                     (Noun (Adj delicious)
                                           (Noun pickle)))))
                         (PP (Prep on)
                             (NP (Det a)
                                 (Noun sandwich))))))))
      !)
# number of parses = 196

Example 3:
(ROOT is
      it
      true
      that
      (S (NP (NP (Det every)
                 (Noun sandwich))
             (PP (Prep in)
                 (NP (Det a)
                     (Noun chief
                           of
                           staff))))
         (VP (Verb wanted)
             (NP (Det a)
                 (Noun floor))))
      ?)
# number of parses = 1

Example output of grammar3.gr:
Example 1:
(ROOT (S it
         (AV perplexed)
         (NP (Det a)
             (Noun (Adj perplexed)
                   (Noun sandwich)))
         (SS that
             (NP (NP (Det every)
                     (Noun floor))
                 (PP (Prep with)
                     (NP (NP (Det the)
                             (Noun president))
                         (Con and)
                         (NP (NP (Det the)
                                 (Noun chief
                                       of
                                       staff))
                             (PP (Prep under)
                                 (NP (Det every)
                                     (Noun president)))))))
             (VP (Verb ate)
                 (NP (Det a)
                     (Noun desk)))))
      !)
# number of parses = 5

Example 2:
(ROOT is
      it
      true
      that
      (S (SS that
             (NP (Det the)
                 (Noun floor))
             (VP (IVP (Intrans sighed)
                      (PP (Prep in)
                          (NP (Det a)
                              (Noun proposal))))))
         (AV perplexed)
         (NP (Det a)
             (Noun (Adj pickled)
                   (Noun floor))))
      ?)
# number of parses = 1


We can see that the sentence with mutiple consecutive proposition phrases usually have much more parses the other. The more propositional phrases the sentence have, the more parses the sentence can have. The different parses come from different combination of proposition phrase and noun: as eacb proposition phrase contain a noun, the propositional phrase can be describing every noun appearing previously in the propositional sequence, resulting in more possibilities of parsing. For grammar.gr, as the weights for NP NP PP rule is not adjusted, the sentence produced has a high chance of having multiple proposition phrases, while in grammar3.gr the weights for that rule is reduced. Sentences with grammar.gr can have really long sentences with lots of parsing choices, while those with grammar3.gr are usually short and only have 1 parsing choice. Even though there are multiple choices, the proposition phrase sequence is usually consist of only two phrases, making number of parsing options low.

Question 5:
(a) The probability of best parse is the probability that randsent.py will produce a sentence with tree-structure in the specific way indicated by the best parse.

For the first sentence, ROOT is parsed using the rule S . , having probability 1/3, S is parsed using the rule NP VP, having probability 1. NP is parsed using the rule Det Noun, having probability 0.5, Det is parsed using the rule Det the, having probability 1/3. Noun is parsed using the rule Noun president, having probablity 1/6. VP is parsed with the rule Verb NP, having probability 1. Verb is parsed using the rule verb ate, having probability 0.2. NP is parsed with the rule Det Noun, having probability 0.5. Det has the word the and Noun has the word sandwich, with probability 1/3 and 1/6. The probability for the best parse is the product of all these probabilities
1/3 * 1 * 0.5 * 1/3 * 1/6 * 1 * 0.2 * 0.5 * 1/3 * 1/6 = 1/19440, which is 5.1e-05 in the calculator

The probability of producing the sentence is the sum of the probability for producing each possible partition of the sentence. As the sentene have only one possible parse, P(best_parse) = P (sentence)

P(best_parse | sentence) is the probability of randsent.py producing the best parse indicated by the parser given that randsent.py produce the sentence. It should be P (best_prse union sentence) | P (sentence). As there are no other possible parsing of the sentence, the two probabilities should be equal, and the resulting probability is 1.

(b)
The probability is 0.5 means that given that the sentence (every sandwich with a pickle on the floor wanted a president) is produced by randsent, the probability of having the best parse produced by parser is 0.5.
As indicated, the probability of producing the specific parse is 6.202e-10. There is also a other way of parsing the same sentence:
(ROOT (S (NP (NP (NP (Det every)
                     (Noun sandwich))
                 (PP (Prep with)
                     (NP (Det a)
                         (Noun pickle))
             (PP (Prep on)
                 (NP (Det the)
                     (Noun floor))))))
         (VP (Verb wanted)
             (NP (Det a)
                 (Noun president))))
      .)
For this parsing, the probability is 1/3 * 1 * 0.5 * 0.5 * 0.5 * 1/3 * 1/6 * 1 * 1/4 * 0.5 * 1/3 * 1/6 * 1/4 * 0.5 * 1/3 * 1/6 * 1 * 0.2 * 0.5 * 1/3 * 1/6 = 6.202e-10 = P (best_parse)

For the sentence, there are two possible parsing having equal probability. Therefore, given that the sentence is produced, the probability of the specific parse should be exactly 0.5

(c) In the corpus, the probabilities of the two sentence appearing are both 0.5. In the grammar model of language, the probability of producing the first sentence is 5.144e-05, and the probability of producing the second sentence is 1.240e-09. -log(P) of the two sentences are 14.2467 and 29.587, which sum up to 43.8337, which is just log prob in the equation. Dividing by word number (18) yields the cross entropy 2.435.

(d) The perplexity is just exponentiating the cross entropy, which is e^2.435 = 11.4158

(e) The cross entropy here is infinity: as the second setence have a VP with only a verb but not NP, it's not a sentence that can be produced using grammar.gr. The probability of producing that sentence with grammar model is 0, indicating that the log probability is negative infinity. When summing negative log probability, the result is also infinity and produce an infinite cross-entropy

Question 6:
(a) command used: python3 randset.py -n 200 -g grammar2.gr | ./parse -P -g grammar2.gr
The entropy of grammar2 is 2.002 bits per words (4575.336 / 2285)
(b) The entropy of grammar3 is 2.300 bits per words (6761.001 / 2940). Grammar3 has higher entropy than grammar2. This is natural as grammar3 is designed to incorporate more diverse sentence forms and incoporate more word types and choices. Generally, longer sentences can have lower probability (as the product of the partition is the sum of more probabilities at each step of choosing rules). For grammar3 it can have longer sentences due to variety in gramamr rules and sentence forms. All these factors contribute to higher entropy for grammar3 than grammar2.
(c) The resulting entropy is infinity. Obsevations shows that some sentence in the generating process has ... with default max expansion settings (450). We have tried increasing that threshold to 1000, while still having ... in produced sentence. Since the grammar.gr is designed in the way that allow excessively long sentences, the appearane of ... is unavoidable unless having arbitarily large max expansions. As ... is not part of the grammar, all sentence with that will have probability 0 in the model and thus have infinite log probabilities, making cross entropy also infinity.

Question 7
We generate a new corpus for this problem. The entropy of grammar 2 on this corpus is 2.062 (4706.601 / 2282). 
The cross entropy for grammar3 is 2.590. As the sentence that can be produced by grammar2 is a subset of possible sentences for grammar3, the probability of each sentences with grammar2 is higher than the probability of each sentences with grammar3 (the probability of each parse is lower for grammar3, as for each symbol there are more rules to choose). As the probability of the sentence appearing in the corpus remain constant, when negative log probability increase (when probability decrease), the sum of log probability increased, making cross entropy of grammar3 larger than grammar2's entropy

 and the cross entropy for grammaar is 2.205. For grammar, it has higher probability of producing long sentences than grammar2. For corpus generated by grammar2, they are likely to be shorter sentences. The probability of producing thsoe sentences with grammar is lower than the probability of producing thsoe sentences with grammar2. In a similar way, the total log probability for grammar is higher the the cross entropy of grammar is larger than the entropy of grammar2