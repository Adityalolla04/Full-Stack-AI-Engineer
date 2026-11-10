# PACELC

[Back to HLD](../README.md) · [Your practice space](practice/README.md)

## In simple words

PACELC extends the discussion: during partitions consider availability versus consistency; otherwise consider latency versus consistency.

## What to understand

Replication coordination can add delay even when the network is healthy. State the system's configuration and operation being analyzed.

## Think through this example

Waiting for a distant replica can improve a consistency guarantee while increasing normal write latency.

## Common mistake

Treating PACELC as a product label independent of configuration.

## Practice yourself

Compare local acknowledgment with cross-region acknowledgment under normal operation and failure.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[Daniel Abadi on PACELC; supplementary original notes](https://dbmsmusings.blogspot.com/2010/04/problems-with-cap-and-yahoos-little.html). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
