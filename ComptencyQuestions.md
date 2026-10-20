# THE FEDERALIST: RESEARCH QUESTIONS AND KEY NOTIONS

## KEY NOTIONS

Agent · AgentRole · Event · Document · Record · Computation · Reference · TemporalExtent · Place · Quantity

## TYPES

- Event: Writing, Publication, Sending, Shipment
- Document: Essay, Collection, Letter, Volume, Edition, AuthorshipList, Newspaper, Study
- Role: Author, Sender, Recipient, Shipper, Receiver, Intermediary
- Reference: MentionsFederalist, MentionsPublius, MentionsAgent, NamesAuthors, RefersToEssay, Opinion, PrintingProblem

Every Event, AgentRole and Reference is a Record based on a source Document.
Each essay has one Writing event. Each source adds its own Author role to it.
(computed) = we work it out from records; no source states it.

## MODULE 1: ESSAYS AND AUTHORSHIP

1. Which essays does source S credit to agent A?

   List version: for essay N, whom does source S name as author?

   [Agent, performsRole, AgentRole(Author), Event(Writing), Document(Essay), isDirectlyBasedOn, Document(source)]

2. What newspaper published essay N, and on what date, according to each source?

   [Document(Essay), Event(Publication), inVenue, Document(Newspaper), TemporalExtent, isDirectlyBasedOn, Document(source)]

3. Which essays are disputed, and which source names whom? (computed: sources name different authors)

   [Document(Essay), Event(Writing), AgentRole(Author), Agent, isDirectlyBasedOn, Document(source), generatedBy, Computation]

4. Which essays does one source credit to two or more agents? (computed)

   [Document(Essay), Event(Writing), AgentRole(Author), Agent, isDirectlyBasedOn, Document(source), generatedBy, Computation]

5. For an author claim, which source is it based on, what kind of document, who made it, and when?

   If unknown, "not recorded".

   [AgentRole(Author), isDirectlyBasedOn, Document, hasDocumentType, attributedTo, Agent, TemporalExtent]

<!-- Preserve the supplied question numbers when rendered as Markdown. -->

7. Which essays does every source credit to the same agent? (computed)

   [Document(Essay), Event(Writing), AgentRole(Author), Agent, isDirectlyBasedOn, Document(source), generatedBy, Computation]

8. How many essays does source S credit to each agent? (computed)

   [Document(source), AgentRole(Author), Agent, Event(Writing), Document(Essay), generatedBy, Computation]

## MODULE 2: LETTER NETWORK

11. Which letters mention the Federalist or "Publius", and who sent each one to whom?

    [Document(Letter), Reference(MentionsFederalist, MentionsPublius), Event(Sending), AgentRole(Sender, Recipient), Agent]

12. Which letters about the Federalist did agent X send or receive, and when?

    Follow-up: only those received on date Y.

    [Agent, performsRole, AgentRole(Sender, Recipient), Event(Sending), Document(Letter), TemporalExtent]

13. Which letter is a reply to which?

    [Document(Letter), isReplyTo, Document(Letter), TemporalExtent]

14. Where was each letter sent from, and where to? If unknown, "not recorded".

    [Event(Sending), Document(Letter), fromPlace, Place, toPlace, Place]

15. Which letters were sent while the essays were still being printed? (computed: Oct 1787 to May 1788)

    [Event(Sending), TemporalExtent, Event(Publication), generatedBy, Computation]

16. Who else is named in a letter, besides the sender and the recipient?

    [Document(Letter), Reference(MentionsAgent), refersTo, Agent]

17. Where does our text of each letter come from?

    [Document(Letter), isDirectlyBasedOn, Document, hasDocumentType]

## MODULE 3: WHAT THE LETTERS SAY

19. Who sent copies of which volume, how many, to whom, through whom, and when?

    [Event(Shipment), Document(Volume), Quantity, AgentRole(Shipper, Receiver, Intermediary), Agent, TemporalExtent, isDirectlyBasedOn, Document(Letter)]

20. Which essays does a given letter refer to, and what passage says so?

    [Document(Letter), Reference(RefersToEssay), refersTo, Document(Essay), Passage]

21. For agent P, what is the earliest letter that names the authors and has P as sender or recipient?

    If none, "no evidence". (computed)

    [Agent, AgentRole(Sender, Recipient), Event(Sending), Document(Letter), Reference(NamesAuthors), TemporalExtent, generatedBy, Computation]

22. Which author claims come from letters rather than lists or editions, and who sent each letter to whom?

    [AgentRole(Author), isDirectlyBasedOn, Document(Letter), Event(Sending), AgentRole(Sender, Recipient), Agent]

23. Which letters give an opinion of the Federalist, and what passage says so?

    [Document(Letter), Reference(Opinion), refersTo, Document(Collection), Passage]

24. Which letters mention a problem with the printed book, and what passage says so?

    [Document(Letter), Reference(PrintingProblem), refersTo, Document(Volume), Passage]
