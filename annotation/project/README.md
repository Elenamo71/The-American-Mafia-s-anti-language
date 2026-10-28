# CATMA project export (to deposit)

Export from CATMA 7.2.3: *Project → Export → TEI (stand-off)*, including every
document and every annotation collection used in Chapter 8.

* Keep the document names identical to the `file_id`s (`CA2C_001`, …).
* Include both annotation passes (pass 1, pass 2) as separate collections.
* If the exploratory tagsets (*Trust*, Conceptual Metaphor) remain in the project,
  say here that they were **not used** in the thesis.
* Add a CSV flattening of the spans (`../concordances/speech_acts.csv`) so that
  readers without CATMA can use the data.
