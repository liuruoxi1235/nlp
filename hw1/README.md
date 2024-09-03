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
First, it is obviously more common for people to use periods to end setences than to use exclamation marks or "Is it true that ... ?" structure. The exact percentage for these three sentence types depends on the context, but in general period-ended sentences make up 70-90% of English sentences while exclamation-mark-ended sentence only around 5%. So we give (ROOT -- S .) a weight of 70, (ROOT -- S !) a weight of 5, and (ROOT	-- is it true that S ?) only 0.5 since it is apparently rarer to appear. Also, "the" and "a" are more commmon determiners than "every", but "every" certainly appear on a regular basis in English, so we gave "the" and "a" each a weight of 5 and "every" a weight of "1". The same is done with prepositions, where we gave a smaller weight to "under" than "with", "on", and "in". 

Question 5

the fine perplexed chief of staff wanted the pickle . 

the pickled pickle ate a pickle in the perplexed chief of staff ! 

every pickle wanted a chief of staff . 

the pickled perplexed perplexed chief of staff in every president ate the pickled perplexed pickled perplexed fine sandwich . 

a sandwich ate the pickled sandwich . 

a pickled chief of staff understood a president . 

the chief of staff kissed a chief of staff in the pickled president . 

the sandwich kissed a floor . 

is it true that a floor understood the pickle ? 

the perplexed pickle kissed a sandwich on a floor on the pickled fine sandwich with the pickle . 

2.3
Question 9:
Modifications: We made several modifications to handle the grammatical phenomena in this question. First, we distinguish between names and other nouns, since all nouns except names require a determiner before them. Second, 
We distinguish between intransitive and transitive verbs, since only the latter verbs require nouns after them. We
also defined specific sentence rules to allow sentences that have sub-sentences in them using 'that'. As explained in detail below, this involves several sentence structures and defintions of special verbs -- sentence verbs (such as 'thought') that leads sub-sentences, and causative verbs that describe the result of the subsentence. This distinction is also necessary, because it generally doesn't make sense to use normal verbs at these positions (for instance, 'it SAW the president that a pencil lies on the ground" or 'the president ATE that a pencil lies on the ground'.) Here are discussions of each sentence in questions 2.2 and how our grammar addresses it:

sentence 1: 
NP -- Name
Name -- Sally
This is to ensure that NP can be formed with either an normal Noun with an article or just a name (article is not needed). As name is a special kind of noun, a different category need to be established.

sentence 2:
Verb -- Verb Con Verb
NP -- NP Con NP 
Con -- and
This is to make that NP can be formed with two NP combining together with "and" and two transitive verbs can be combined together to be the verb for the whole sentence

sentence 3:
VP -- IVP
IVP -- Intrans-verb
Intrans-verb -- sighed
Intrans-verb -- worked
We created IVP to represent phrases begining with an intransitive verb. In the case of sentence 3, the IVP is only consist of an intransitive verb.

sentence 4:
S -- NP Verb_sentece SS
Verb_sentence -- thought
SS -- that NP VP
We created a type called SS (stands for sub-sentence that is consist of that, NP and VP). In this case, the whole sentence will serve as a Noun in the sentence. For sentences like sentence 4, a transitive verb is needed and followed by a sub sentence. However, the verb here is different from normal transitive verb: for verbs like thought, its unreasonable to have "I thought Sally", but reasonable for "I thought that (a sentence)". This kind of verb can only get followed by a sentence, and we decide to have a different type of verb for that.

sentence 5:
S -- it CV NP SS
CV perplexed
For sentences like sentence 5, we found that the verb is a different type: it is a adjective but act as a verb in the sentence (it perplexed Michael = it makes Michael perplexed), describing a causal effect of the sub-sentence. This type of verb is special and need a distinctive type. Then, the sentence is consist of it, CV, NP and a substance.

sentence 6:
S -- SS CV NP
Sentences like sentence 6 are similar to sentence 5 but just different in the order of the components: for sentence 6 it put the sub sentence at the beginning and does not need "it" at the beginning.

sentence 7:
Adj -- Adv Adj
Adv -- very
Sentences like sentence 7 introduce adverb that can be used to describe adjective. This type of word need a different category and Ajd can be formed with an ad verb and an adj

sentence 8
IVP -- Intrans-verb PP
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
It's somehow impossible for neural networks to have a concept like noun phrase or verb phrase (definitely neural network don't have mind, just mean that they do not use these concepts to form natural langauge outputs). However, the grammar will represent some patterns of words' combinations (for example, they often found proposition after a noun, while never a noun after an intransitive verb), and can definitely learn these patterns in the process of traning. Also, as sequencial data processing neural networks (like LSTM) and Multi-head attention mechanism of Transformmers allow neural network to "memorize" and refer to long previous context when formming outputs, also allowing neural networks to learn "longer" grammar patterns (for instance, NP VP sentence structure can have a very long NP)

Possibilities of understanding unnatural languages
It might be possible for neural networks to learn such languages: they are learning through combinations of different word patterns, and the grammar is just a higher level rule governing those word patterns. It's more like an abstract concept that guides natural language, while neural networks are learning through lower level word patterns. For unnatural languages, as long as their word formation have recognizable patterns (if there isn't pattern for words sequence, then the language should be similar to nonsense), neural networks will be able to learn such pattern. For human babies, they learn language in a similar way with neural network: instead of learning grammar first, they learn the langauge through mimicing their parents' pronunciation in the beginning, and then learning from the sentences and articles they read. For unnatural languages, they can still learn in this way. Whether the langauge have a grammar or not is not that important. For native speakers of a langauge, they usually does not have a clear concept about grammar, while still able to write grammarly correct sentences. Grammar is more abstract than the actual way for neural network and human infants to learn language. 

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

(d) The perplexity is just exponentiating the cross entropy, which is 2^2.435 = 5.40764333

(e) The cross-entropy here is infinity: as the second sentence has a VP with only a verb but not NP, it's not a sentence that can be produced using grammar.gr. The probability of producing that sentence with the grammar model is 0, indicating that the log probability is negative infinity. When summing negative log probability, the result is also infinity and produces an infinite cross-entropy

Question 6:
(a) command used: python3 randset.py -n 200 -g grammar2.gr | ./parse -P -g grammar2.gr
The entropy of grammar2 is 2.002 bits per word (4575.336 / 2285)
(b) The entropy of grammar 3 is 2.300 bits per word (6761.001 / 2940). Grammar 3 has higher entropy than grammar 2. This is natural as grammar3 is designed to incorporate more diverse sentence forms and incorporate more word types and choices. Generally, longer sentences can have a lower probability (as the product of the partition is the sum of more probabilities at each step of choosing rules). For grammar3 it can have longer sentences due to variety in grammar rules and sentence forms. All these factors contribute to higher entropy for grammar3 than grammar2.
(c) The resulting entropy is infinity. Observation shows that some sentence in the generating process has ... with default max expansion settings (450). We have tried increasing that threshold to 1000, while still having ... in produced sentence. Since the grammar.gr is designed in a way that allows excessively long sentences, the appearance of ... is unavoidable unless having arbitrarily large max expansions. As ... is not part of the grammar, all sentences with that will have probability 0 in the model and thus have infinite log probabilities, making cross entropy also infinity.

Question 7
We generate a new corpus for this problem. The entropy of grammar2 on this corpus is 2.062 (4706.601 / 2282). 
The cross-entropy for grammar3 is 2.590. As the sentence that can be produced by grammar2 is a subset of possible sentences for grammar3, the probability of each sentence with grammar2 is higher than the probability of each sentence with grammar3 (the probability of each parse is lower for grammar3, as for each symbol there are more rules to choose). As the probability of the sentence appearing in the corpus remains constant when negative log probability increases (when probability decreases), the sum of log probability increases, making the cross-entropy of grammar3 larger than grammar2's entropy and the cross entropy for grammar is 2.205. For grammar, it has a higher probability of producing long sentences than grammar2. For corpus generated by grammar2, they are likely to be shorter sentences. The probability of producing these sentences with grammar is lower than the probability of producing these sentences with grammar2. Similarly, the total log probability for grammar is higher the the cross entropy of grammar is larger than the entropy of grammar2 and the cross entropy for grammaar is 2.205. For grammar, it has higher probability of producing long sentences than grammar2. For corpus generated by grammar2, they are likely to be shorter sentences. The probability of producing thsoe sentences with grammar is lower than the probability of producing thsoe sentences with grammar2. In a similar way, the total log probability for grammar is higher the the cross entropy of grammar is larger than the entropy of grammar2

4.1

(a) a/an 
We add the following rules:

1   A   a 
1   An  an

1   Adj_an ambivalent
1   Adj_an excellent

1   Noun_an apple
1   Noun_an orange

We categorize a/an as a separate type apart from other articles. As a/an can possibly be followed by adjectives, nouns, we have a different category for adjectives and nouns that should be proceed by a and an respectively

1   Noun_P A_Noun_P
1   Noun_P An_Noun_P

1   A_Noun_P Noun
0.5   A_Noun_P Adj_a Noun_P

1   An_Noun_P Noun_an
0.5   An_Noun_P Adj_an_P An_Noun_P

The NP that should be proceed by a and an should have a separate type. We name them as A_Noun_P and An_Noun_P. For A_Noun_P, it can be either formed with a single a-noun, or a a-adjective and any noun. To make it more conveinent, we use a type Noun_P to refer to the combination of A_Noun_P and An_Noun_P. As we do not want excessively long consecutive adjectives, we reduce the weight for the resurive one.

1  Adj_an_P Adj_an Adj_an_r
1  Adj_an_P Adj_an

1  Adj_a Adv Adj

1  Adj_an_r Adj_an
0.5  Adj_an_r Adv Adj_an

For adding adverb before a adjective that should proceed with an, we need to be careful as adding adverb at the front will change the an at the front to an. To change this, we make sure that Adj_an_P either have only a single an-adjective or begin with an an-adjective and other adverb-adjective combinations (adj_an_r can have a single an-adjective or proceed by any amound of adverb). This is to ensure that the first adjective of a adjective sequence proceed by an is an an-adjective without adverb. Adverb followed by any adjectives should be considered a an a-adjective

0.5 Det_Phrase Det Noun_P
0.5 Det_Phrase A A_Noun_P
0.5 Det_Phrase An An_Noun_P
1  Adj Adj_a
1  Adj Adj_an

1	NP	Det_Phrase(modified from 1 NP Det Noun)

We change the original Det Noun combination to a Det_Phrase to handle all the phrase start by article. For normal article, they can have any noun afterward. a can only get followed by A_Noun_P, An can only get followed by An_Noun_P.  

(d) We add the following rules:
The clarification of each letter/phrases is explained below.
Q  = question
Wh = interrogative words
AUV = auxiliary verbs (did)
WHVerb = verbs in correct forms that are used in Wh questions after auxiliary verbs 
5 ROOT  Q 

1   Q   Wh AUV Whs
1   Q   Wh AUV Whs that NP Verb
1   Q   Wh AUV Whs NP Prep
1   Q   Wh Verb NP

1   WHVerb  think
1   WHVerb  eat
1   Wh what
1   Wh who
1   Wh where
1   AUV did

Note that the given WH-word questions generally have the following forms: 
They all ends with "?"; Thus, it is crucial to distinguish them with regular sentences which may ends with others such as "." or "!".
Wh-word + did + NP + WHVerb (not past tense) + ?
Wh-word + did + NP + WHVerb + that + NP + Verb ?
Wh-word + did + NP + WHVerb + NP + Prep + ?
Wh-word + Vern + NP + ?
Wh-word + did + NP + WHVerb + NP + ?

Besides, for questions that starts with Wh-words, it is quite easy to distinguish them from other sentences since after the root, it follows Q, but not S.
Thus, we can easily avoid conflicts occur in some sentences. The grammatical pattern of suborninate clause in Wh-word sentecnes, or questions, are quite different from the usual sentences. Thus, we decide to split the common sentence construction with the question constrcution. Ex. the parser cannot parse Sally ate, but it indeed occurs after "that" (what did the president think that Sally ate ?).