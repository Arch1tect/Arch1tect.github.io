---
date: "2013-03-12 05:31:21"
title: EECS376 Foundations of Computer Science Midterm Review
---

A post about *Foundations of Computer Science* midterm review. Finite automata and Turing machines are the two major parts of this exam.

![](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/03/Screen-Shot-2013-03-11-at-8.27.48-PM.png)

# Closure

Regular remains regular under the regular operation:

Union    Concatenation     Star

# Projection

{A x B x C }  = >  {A × C}

# Regular expressions

\*\*\*\*Formal definition:

---

1. a for some a in the alphabet Σ
2. ε
3. Ø
4. (R1 ∪ R2), where R1 and R2 are regular expressions
5. (R1 ∘ R2), where R1 and R2 are regular expressions
6. (R1\*), where R1 is a regular expressions

-   R ∪ Ø = R - Adding the empty language to any other language will not change it
-   R ∘ ε = R - Joining the empty string to any string is the same string

## DFA to Regex **is aided by a special type of finite automata, called a generalized nondeterministic finite automaton defined as the following 5-tuple (Q, Σ, δ, qstart, qaccept)**

# [**Pumping Lemma**](http://stackoverflow.com/questions/461619/in-laymens-terms-what-is-the-pumping-lemma/1933405#1933405)

The Pumping Lemma can be used to show that a language is infinite. (given the language is regular)  
 True. If a language is regular and contains a suciently long word, then it can be pumped, and is therefore innite.

Any language over the singleton alphabet {a} is regular.  
 False. (See Example 1.76 in text.)

Any subset of a regular language is regular.  
 False. For example, sigma∗ is regular; the claim is that any language is regular.

A DFA contains a reachable loop i its language is innite.  
 False. For example, the DFA need not have any accepting state. [Most people missed this and the question was not scored.]

For any fixed pattern p, there exists a DFA/NFA M, such that, for any input w, M accepts w i p occurs in w.” T

Given any q-state DFA, there is an equivalent NFA with at most 2^q states.  
 True. A DFA is an NFA.

When building a DFA for a single language, sometimes the number of states should depend on the length of the input.  
 False. The denition of DFA requires that \there exists a machine such that, for all input…”

![](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/03/Screen-Shot-2013-03-12-at-4.32.03-AM.png)

When simulating a two-tape TM M by an ordinary TM M′, for any M, one can always arrange that the head positions of M can be determined from the head position of M′ and the state of M′.  
 False. There are innitely many possible head positions for M′, which cannot be recorded in the nite state space of M. The head of M must be free to move and cannot code anything.

When simulating a two-tape TM M by an ordinary TM M′, for any M, one can always arrange that the head positions of M can be tracked by making the tape alphabet of M′ include two versions (two fonts) of the  
 tape alphabet of M and recording whether or not a head is in a cell by choice of font in that cell.  
 True.

When simulating a two-tape TM M by an ordinary TM M′, for any M, one can always arrange that the number of states in M′ is at most twice the number of states in M.  
 False. In general, M′ needs to shuttle back and forth and remember all sorts of things. Doubling the number of states lets M′ record exactly one more bit, assuming the state of M is coded into the state of M′.  
 There is another approach whereby the state of M is coded into the tape of M′. Either this would not be an ordinary TM (e.g., the program of M is given as an auxiliary input, say, on a separate tape, as in the case of a universal TM) or the number of states in M′ would still exceed twice the number in M (e.g., the transition function of M|the static program of M, as opposed to the dynamic runtime state of M|is coded into the transition function of M′.

A 2-tape Turing Machine can recognize the language of strings of the form a+b = c over the alphabet {0;1;+;=}, where the addition holds if strings a; b; c are interpreted as binary numbers.  
 True. **(But not a DFA.)**

The regular languages are closed under complement. Although computing the complement is easy in some models of computation (including on DFAs), it is costly in the NFA model, which is the right model for  
 thinking about the other regular operations.

The set of recognizable languages is closed under projection.  
 The set of decidable languages is not closed under projection.

**winning the game as Peggy does not say a language is regular, just that it might not be ..not regular.**

# Turing machines

\*\*\*\*Differences between a Turing Machine and finite automata:

---

1. A Turing Machine can both read from / write to the tape.
2. The read-write head can move both left and right.
3. The tape is infinite.
4. The special states for accepting/rejecting take effect immediately.

\*\*\*\*Formal Definition:  
 A Turing machine is a 7-tuple (Q, Σ, Γ, δ, q0, qaccept, qreject)

---

1. Q is the set of states
2. Σ is the input alphabet not containing the blank symbol ⊔
3. Γ is the tape alphabet where ⊔ ∈ Γ and Σ ⊆ Γ
4. δ is Q x Γ → Q x Γ x {L, R} is the transition function
5. q0 ∈ Q is the start state
6. qaccept ∈ Q is the accept state
7. qreject ∈ Q is the reject state where qreject ≠ qaccept

\*\*\*\*When talking about Turing Machines there are 3 main kinds that we speak of:

---

1. Decider: A turing machine that halts on all inputs(either accepts or rejects). These are similar to a DFA in that sense.
2. Recognizer: A turing machine that either reaches accept or loops. A recognizer can run infinitely (see the Halting Problem). They are also the default for a turing machine
3. Enumerator: Lists elements of a language rather than considering strings.

Turing-recognizability means that there is a program that can confirm that a string w is in a language, and co-Turing-recognizability means that there is a program that can confirm that a string w is *not* in the language.

A language is decidable iff it is Turing-recognizable and co-Turing recognizable

Part of the notes are from google doc class collaboration
