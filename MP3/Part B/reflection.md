# MP3 Part B Reflection

## What Did I Productize?

I productized the MiniClaw gear and print-readiness review that I was doing
manually across the ACME corpus. The skill now tells the AI when to check
`ACME-ENG-001` gear limits, BigClaw wall-thickness precedent, Prusa MK4S
tolerances, PLA+ interlayer stress, and the `ACME-ENG-003` tolerance stack. The
MCP tool turns those checks into a repeatable query path, such as the logged
question about a 12T module 1.0 pinion with 0.08 mm backlash.

## Where Does The Stack Break?

The stack breaks when the CAD screenshot lacks dimensions that the AI needs for
a real engineering calculation. Example query: "Does this jaw arm pass bending
stress at full grip force?" If the screenshot does not include arm length,
section thickness, load, print orientation, and material process, the MCP tool
can retrieve useful ACME limits but cannot prove the part is safe.

## Trust Ledger

The skill helped the AI succeed during Checkpoint 1 by forcing it to compare
the first housing against MiniClaw-specific sources instead of treating the
BigClaw as a direct copy target. The logged BigClaw query retrieved
`ACME-VND-002`, and the CAD writeup used that chunk to change load-bearing
walls from 1.0 mm to 2.0 mm.

The AI still did something I did not fully accept: after Checkpoint 2 it pushed
toward increasing the output gear again for more mechanical advantage. The
skill did not catch that this conflicted with my compact-envelope goal, so I
overrode that suggestion and kept the 14T-to-84T gear pair while adding only
print-orientation and single-piece gear-cavity notes.
