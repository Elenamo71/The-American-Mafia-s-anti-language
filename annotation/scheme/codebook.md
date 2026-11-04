# Coding manual

This manual operationalises the scheme in thesis Appendix N for use by a second
coder. Definitions are taken from the dissertation; the section references are
to the thesis. Lines marked **⚑ decide** are decision rules the thesis does not
state explicitly. The author must settle them *before* the reliability study,
because they are the most likely sources of disagreement.

Machine-readable version: [`tagset.csv`](tagset.csv).

## 0. Units and context

* A **unit** is the target segment shown in `sample_for_coder.csv`, read
  together with the preceding and following segments.
* Transcription marks follow the FBI conventions (thesis Table 1.4): `[U/I]`,
  `[ph]`, `[inaudible]`, `[NAME]`, `...`, `--`. Do not correct or normalise the text.
* **⚑ decide**: if a unit contains more than one act (e.g. *"Fuck him. Tell him I
  want five."*), code the **dominant** act, the one the rest of the turn serves,
  and record the secondary act in `coder_note`.

## 1. Speech-act type (Searle, 1969; thesis § 3.4, Appendix N §1)

| Code | Definition | Corpus example |
|---|---|---|
| `assertive` | Commits the speaker to the truth of a proposition (stating, reporting, describing) | *"There was a settlement."* (EDNY_003) |
| `directive` | Attempts to get the hearer to do something (order, request, instruction, prohibition) | *"Freeze it."* (CA2C_001) |
| `commissive` | Commits the speaker to a future course of action, including threats and promises | *"I'll put you right in the ground."* (SDNY_001) |
| `expressive` | Expresses the speaker's attitude toward a person or state of affairs; here mainly insults and status-lowering labels | *"You dumb fuck."* (EDNY_010) |
| `none` | Back-channel, fragment, question without directive force, or not interpretable | *"Yeah, yeah."* |

Rules:

* Code the **illocutionary force in context**, not the grammatical mood. An
  assertive surface can carry a directive force: *"This guy is no good anymore"* →
  `directive` (thesis Appendix N).
* **⚑ decide – threats with an implied order.** Appendix I counts some
  first-person threats as directives, e.g. *"I will break every bone in his fucking
  hands so he can't work"* (row 70) and *"I'll come down and fuckin' crack his head
  real quick"* (row 76). Choose and state one rule: either (a) a first-person
  future of violence is `commissive` unless an addressee is instructed to act, or
  (b) code the force the speaker is pursuing toward the hearer. Rule (a) is more
  replicable.
* **⚑ decide – reported directives.** Is *"He said tell this fucking kid to bring
  some fucking dough"* (row 47) a directive by the current speaker or a reported one?
* **⚑ decide – rhetorical questions.** *"Who the fuck's he think he is?"* (Appendix J)
  is listed as an expressive. Confirm that rhetorical questions of contempt are
  `expressive`.

## 2. Directive mitigation (Brown & Levinson, 1987; Culpeper et al., 2017; § 8.2.2)

| Code | Definition |
|---|---|
| `bald-on-record` | Performed directly with no politeness device (bare imperative, *I want…*, *you gotta…*, *better…*) |
| `mitigated` | Contains a politeness device: *please*, conditional or interrogative request (*could you…*, *would you mind…*), hedges, or a suggestion frame |

* In the thesis all three mitigated directives are *please* + bare imperative.
  Code them `mitigated`; the thesis treats this as the upper bound.
* **⚑ decide**: are aggravators (repetition, profanity, deadlines) relevant here?
  The thesis treats them as features of bald-on-record directives, not as a
  separate value.

## 3. Commissive orientation and conditionality (§ 8.3.2)

* `prospective`: the threatened act lies in the future (*I'll…*, *I'm gonna…*).
* `retrospective`: the act is registered as past or counterfactual (*I should've…*).
* `other`: present tense or non-modal.
* Conditionality (Muschalik, 2018): `manipulative` if a compliance path is stated
  (*if/next time you don't pay…*); `retaliative` if not.

## 4. Expressive directness (§ 8.4.2; Figure 8.4)

The thesis describes these criteria as surface-diagnosable and usable by a second
coder. Apply three questions in order:

1. Is the unit a derogatory predication of a person? If not → `E0` (narrated
   violence, idiom, situation label, bare directive).
2. Is the target the addressee (second person)? If yes → `D3` bald-on-record
   (*you fucking jerkoff*).
3. Is the target a third party present in the speech situation? If yes → `D2`
   on-record present (*this douchebag*). Otherwise, or if the derogation is
   reported from an earlier exchange → `D1` off-record displaced (*he's a
   cocksucker*, said of an absent party).

## 5. Slurs (§ 9.1; Table 9.3)

* `contains_slur`: yes / no.
* `slur_sentiment`: `hostile` if the term is used to degrade its referent here;
  `neutral` if it is used referentially or as in-group banter.
  **⚑ decide**: how to code taboo intensifiers (*fucking*) that do not target a
  person. Proposed rule: these are not slurs (category = taboo intensifier,
  sentiment n/a).
* `referent_group`: `ingroup` (members, the Family) or `outgroup` (state, law
  enforcement, informants, civilians).

## 6. Organizational context (§ 8.3.2; Appendix N §6)

* `intra-family`: speaker and target/addressee belong to the same Family or the
  same chain of authority.
* `inter-family`: they belong to different Families.
* `civilian`: the target/addressee is not a member (victim, debtor, businessman).
* Use `corpus/metadata/corpus_metadata.csv` (speakers, family) and the context.
  If membership cannot be established from the transcript and metadata, write
  `unknown`. **Do not guess.**
