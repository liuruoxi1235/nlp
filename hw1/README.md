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
The mainly responsible grammar rule for long sentences is NP NP PP. As this grammar rule make recursive definition of NP: if this rule is choose for new NP in previous NP, the pattern will repeat util finally the other rule of NP (NP, Det, Noun) is chosen at some part. Also, as the only rule for PP is Prep and NP, it will generate another NP in the sequence, also facing the previous situation. This is likely to cause the sentence to be very long, as NP pattern can extend unlimitedly.

Question 2
For Noun, the possible rules in current grammar are (adj, Noun), and each noun words (total 5). The chance of choosing adj and Noun rule is only 1/6, and having consecutive adjectives means choosing two adj & Noun rule consecutively. The chance is only 1/36.

Question 3
Should make the weight for NP NP PP rule smaller, and the weight for Noun Adj Noun rule larger

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
S  NP Verb SS
SS that NP VP
We created a type called SS (stands for sub sentence that is consist of that, NP and VP). In this case, the whole sentence will serve as a Noun in the sentence. For sentences like sentence 4, a transitive verb is needed and followed by a sub sentence.

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