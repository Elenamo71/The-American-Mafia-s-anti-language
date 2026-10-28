# Transcripts

18 files, one per row of thesis Table 1.3 (`file_id` = file name without `.txt`).

* **Content.** Intercepted conversations quoted in the PACER filings listed in
  `../metadata/corpus_metadata.csv`, extracted after OCR (ABBYY FineReader, UPDF)
  and manual verification.
* **No normalisation.** FBI transcription conventions (`[U/I]`, `[ph]`,
  `[inaudible]`, `[NAME]`, `...`, `--`) and non-standard spelling are preserved
  as in the source (thesis § 1.4.2, Table 1.4).
* **Encoding.** UTF-8. Most files keep Windows (CRLF) line endings. The files are
  stored byte-for-byte (`.gitattributes`: `-text`) and can be verified with
  `sha256sum -c ../metadata/SHA256SUMS`.
* **Rights.** The text reproduces U.S. federal court records. No additional rights
  are claimed in it; the CC BY 4.0 licence of this repository does not apply to it.
* **Personal data.** Third parties are named. Data-protection decision: _to be
  recorded here after consulting the University of Alicante's Data Protection
  Officer (dpd@ua.es)._
