# MiniClaw MCP Conversation Export

**Host:** Codex local MCP-style test harness  
**Skill loaded:** `MP3/Part B/skills/miniclaw_gear_dfm_review.md`  
**Tool connected:** `query_miniclaw_rag` from `MP3/Part B/mcp_server/server.py`

## Exchange 1 — Gear Face Width

**User:** I am reviewing a MiniClaw 12T-to-72T gear pair in PLA. The pinion is
module 1.0 with a 4 mm face width and 0.08 mm backlash. What should I change
before committing the CAD?

**Host tool indicator:** calling tool `query_miniclaw_rag`

**Tool question:** MiniClaw PLA gear module 1.0 face width backlash ACME-ENG-001

**Retrieved context:** `ACME-ENG-001` says preferred printed gear modules are
0.8, 1.0, and 1.25; module 1.0 gears need at least 14 teeth; production face
width should be 4-6x module; PLA gear backlash should be 0.10-0.15 mm. The
same standard says to add 0.05-0.10 mm to center distance for thermal growth
and print tolerance.

**AI answer:** The 12T module 1.0 pinion fails the ACME tooth-count rule; use
at least 14 teeth or increase module/ratio elsewhere. The 4 mm face width is
inside the production range, so I would keep that part. The 0.08 mm backlash is
too tight for PLA; set nominal backlash to at least 0.10 mm and consider a
0.05-0.10 mm center-distance allowance.

## Exchange 2 — Jaw Housing Wall Thickness

**User:** My first OpenSCAD housing uses 1.0 mm PLA side walls because the
BigClaw teardown measured walls around 0.8-1.2 mm. Is that okay for MiniClaw?

**Host tool indicator:** calling tool `query_miniclaw_rag`

**Tool question:** BigClaw teardown PLA wall thickness MiniClaw housing

**Retrieved context:** `ACME-VND-002` says BigClaw uses hard aluminum alloy
with 0.8-1.2 mm walls, and warns that ACME PLA designs must use at least
1.5 mm walls and probably 2.0 mm in load-bearing areas.

**AI answer:** Do not copy the BigClaw wall thickness into the MiniClaw
housing. BigClaw's walls work because they are machined aluminum. For MiniClaw
PLA, revise the load-bearing side walls to 2.0 mm and use 1.5 mm only where
the wall is lightly loaded.

## Exchange 3 — Press-Fit Bore

**User:** The jaw pivot has a 3.00 mm pin and a 3.02 mm printed bore. I want it
to be a light press fit across the RobotExpo run. Is the tolerance realistic?

**Host tool indicator:** calling tool `query_miniclaw_rag`

**Tool question:** MiniClaw printed bore press fit tolerance Prusa MK4S ACME-ENG-003

**Retrieved context:** `ACME-MFG-001` lists press-fit interfaces at +/-0.15 mm
across production, and `ACME-ENG-003` says MiniClaw gear and pivot stack-ups
should be checked against Prusa MK4S process capability, especially dimensions
under 10 mm.

**AI answer:** A 0.02 mm bore offset is not realistic as a controlled press fit
on the Prusa MK4S fleet. Across production, the bore can vary far more than
that. I would redesign the pivot as a clearance fit with a retained pin, or
specify a post-reamed bore if a true press fit is required.
