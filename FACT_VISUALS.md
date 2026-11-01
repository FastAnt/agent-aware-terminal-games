# Fact visuals — design notes (one visual per fact)

Written before the code, per fact (FACTS_REVIEW.md rule: one fact =
one new visual, never reused). Each entry says what the picture
shows and why; the module's `paint()` then implements exactly
that. Status is tracked in FACTS_INDEX.md ("visual: bespoke").

## Batch O1 — orbits group, part 1 (25)

- geometry-fact-great-circle-flights-001 — Sphere with two city
  dots; the great-circle route arcs over the pole, a faint flat
  straight line below the sphere shows the longer map illusion.
- geometry-fact-klein-bottle-001 — A bottle outline whose neck
  enters its own wall; a dot travels the surface and returns
  without crossing an edge: no inside.
- geometry-fact-mobius-cut-001 — A twisted band drawn as two arcs
  with a half-twist; a dot walks the centre line and comes back
  on the "other" side that is the same side.
- geometry-fact-sphere-area-lune-001 — Sphere with two meridians
  forming a shaded lune; the lune's angle is labelled, area
  grows with the angle.
- geometry-fact-spherical-triangle-001 — Sphere, pole, two
  meridians a quarter apart and the equator: a triangle with
  three right-angle marks and "270°" written inside.
- geometry-fact-torus-donut-001 — A cup outline on the left
  morphs by an arrow into a ring with a hole: one handle = one
  hole, genus 1 both.
- physics-fact-chandrasekhar-001 — A horizontal threshold line
  at 1.4 solar masses; calm star dots below it labelled
  "white dwarf holds", a collapsing arrow above it.
- physics-fact-earth-core-hot-001 — Earth in cross-section:
  crust, mantle, liquid outer core, solid inner core; the
  centre is labelled with the Sun-surface temperature.
- physics-fact-great-red-spot-001 — Jupiter's banded disc with
  a wide oval storm; a small Earth circle beside it, visibly
  narrower than the storm.
- physics-fact-hafele-keating-001 — A globe with two flight
  loops, east and west arrows; two clock faces underneath end
  on different times.
- physics-fact-io-volcanic-001 — Large Jupiter, small Io beside
  it squeezed alternately tall and wide (tides), with little
  plume triangles erupting.
- physics-fact-iss-falling-001 — Earth's curved limb, a station
  dot on a circular path with a tangent "falling forward"
  arrow that always misses the ground.
- physics-fact-mars-olympus-001 — Mars disc and, at its limb, a
  very wide, low volcano profile; a small steep Everest
  triangle for contrast with a height ratio label.
- physics-fact-neutron-star-density-001 — A tiny dense sphere
  and a sugar cube outline; arrows compress a mountain ridge
  icon down into the cube.
- physics-fact-ocean-tides-two-001 — Earth centre, Moon to the
  right; the ocean is an ellipse bulging toward AND away from
  the Moon, both bulges labelled.
- physics-fact-sun-fate-white-dwarf-001 — A three-stage
  timeline: medium Sun, swollen red giant, tiny white dwarf
  dot, connected by a slow arrow.
- physics-fact-tidal-locking-001 — Earth and Moon with a face
  mark on the Moon; the mark stays turned to Earth all the
  way around the orbit.
- physics-fact-venus-retrograde-001 — Venus with two curved
  arrows fighting: orbit one way, spin the opposite way,
  labelled "day longer than year".
- geometry-fact-mercator-greenland-001 — Two pairs of bars:
  "on the map" Greenland ≈ Africa, "in reality" Greenland's
  bar is a fourteenth of Africa's.
- geometry-fact-no-perfect-map-001 — A sphere on the left; on
  the right its surface peeled into gores that will not lie
  flat without gaps, "stretch or tear" underneath.
- geometry-fact-winkel-tripel-001 — Three distortion gauges
  (area, angle, distance) as three bars, all pushed to the
  middle on purpose; none at zero, none extreme.
- physics-fact-aurora-sound-001 — Earth's pole with curved
  magnetic field lines; charged dots spiral down them into
  wavy green-less (monochrome) curtain bands.
- physics-fact-continental-drift-rejected-001 — Two continent
  blobs with a widening striped seafloor between them; ridge
  line in the middle, arrows pulling apart.
- physics-fact-dark-matter-rotation-001 — A spiral galaxy disc
  and below it a graph: dashed predicted rotation curve
  falling, solid observed curve staying flat.
- physics-fact-diamond-rain-001 — Neptune as layered disc:
  methane label near top, tiny diamond dots raining down
  through the mantle layer.

## Batch O2 — orbits rest + first network (25)

- physics-fact-earth-rotation-speed-001 — Equator line with a
  speed arrow "1,670 km/h" and a tiny person standing calmly;
  the point: speed without felt acceleration.
- physics-fact-eddington-eclipse-001 — Black Sun disc with
  corona ticks, two star dots whose apparent positions shift
  outward along bent rays.
- physics-fact-fusion-pp-chain-001 — Core dot and a photon
  zig-zagging in tiny steps through dense dots for ages, then
  escaping straight: the random walk out.
- physics-fact-gps-relativity-001 — Earth, one satellite, and
  two clock readouts: satellite "+38 µs/day" vs ground, with a
  position dot drifting when uncorrected.
- physics-fact-gravitational-waves-2015-001 — Two black dots
  spiralling into each other and a chirp waveform below whose
  frequency and amplitude rise.
- physics-fact-great-oxidation-001 — Timeline axis: low oxygen
  flat, then a rising curve labelled "cyanobacteria waste",
  with rust-band dots appearing in rock layers.
- physics-fact-magnetic-reversals-001 — A horizontal stripe
  sequence of alternating light/dark polarity bands (ocean
  floor record), a compass needle flipping above.
- physics-fact-mercury-perihelion-001 — An ellipse whose
  perihelion marker slowly precesses, drawing a rosette;
  "43 arcsec/century unexplained" beside it.
- physics-fact-milankovitch-001 — Three small dials
  (eccentricity, tilt, precession) above a jagged ice-age
  curve that follows their combined rhythm.
- physics-fact-moon-receding-001 — Earth–Moon distance line
  with a laser pulse bouncing to a mirror; the gap grows
  "3.8 cm/yr" and a day-length gauge lengthens.
- physics-fact-pulsar-clocks-001 — A neutron star with two
  lighthouse beams sweeping; a tick strip below with
  perfectly even ticks.
- physics-fact-saturn-floats-001 — A big ringed planet circle
  sitting high on a water line, a density bar showing
  0.69 < 1.0 of water.
- physics-fact-seismic-shadow-001 — Earth cross-section, an
  earthquake star on the left, rays bending through layers
  and a shadow gap on the far side with a small inner-core
  deflection.
- geometry-fact-bernoulli-spiral-tomb-001 — Two spirals side
  by side: self-similar logarithmic (labelled "wanted") and
  evenly spaced Archimedean ("carved by mistake").
- geometry-fact-dymaxion-map-001 — A triangle net of an
  icosahedron partly folded, continent blobs kept whole on
  the triangles, cuts in the "oceans".
- geometry-fact-geodesic-domes-001 — A hemisphere dome of
  triangles with load arrows at the crown flowing down the
  struts to the ground.
- geometry-fact-loxodrome-spiral-001 — A sphere with a course
  line crossing meridians at a constant angle, winding
  tighter and tighter toward the pole.
- geometry-fact-pentagon-soccer-001 — A ball patch: hexagons
  around with exactly twelve pentagon dots highlighted and
  counted as they appear.
- physics-fact-cmb-pigeons-001 — An antenna dish, a noise
  waveform that will not clean up, two pigeon dots being
  shooed, and "2.7 K everywhere" as a baseline.
- physics-fact-olbers-dark-001 — A field of star dots in
  shells; lines of sight end at a horizon marked "finite
  age", beyond it darkness — why the night is black.
- physics-fact-snowball-earth-001 — Earth disc almost fully
  white with a narrow dark equatorial crack of open water,
  CO2 gauge rising beside it toward thaw.
- architecture-fact-byzantine-third-001 — Four general nodes:
  three honest repeating one order, one traitor sending the
  opposite; counter "3 honest > 1 traitor x3 rule".
- architecture-fact-chaos-monkey-001 — A rack of server boxes;
  one randomly flashes and is struck out while traffic arrows
  reroute and the service bar stays green-less "still up".
- architecture-fact-gossip-spread-001 — Dots in a field; an
  informed dot tells a random neighbour each beat and the
  informed colour spreads exponentially.
- architecture-fact-grpc-streaming-001 — One client and one
  server joined by a thick channel carrying arrows both
  ways at once (streams), contrasted with a thin single
  request arrow above.

## Batch N1 — network group, part 1 (25)

- audio-fact-dithering-paradox-001 — Two mini waveforms: clean
  sine, its harsh staircase quantisation, then the dithered
  version where steps dissolve into fine noise.
- cloud-fact-cell-based-001 — A 3x2 grid of identical cells
  (stack, data, routing); one cell is struck out in an
  incident, the rest keep serving.
- geometry-fact-five-platonics-001 — Five solid icons in a
  row (tetrahedron, cube, octahedron, dodecahedron,
  icosahedron outlines) each labelled with its face count.
- geometry-fact-honeycomb-hales-001 — A hexagonal tiling
  filling the frame; one cell outlined heavily with
  "least perimeter per area" beneath.
- geometry-fact-kepler-oranges-001 — Circles packed in
  pyramid rows, each touching its neighbours; a density
  gauge at 74 percent.
- geometry-fact-menger-sponge-001 — A square carpet carved
  recursively: centre removed, then centres of the remaining
  nine, two levels deep, holes within holes.
- geometry-fact-peano-curve-001 — A recursive Hilbert-style
  polyline snaking until it fills a square frame, start and
  end dots marked.
- geometry-fact-sphere-packing-dim8-001 — A central circle
  ringed by touching neighbours, with eight axis ticks
  labelled "dimension 8: E8 proven optimal".
- geometry-fact-tesseract-net-001 — A net of eight square
  "cubes" in a cross (one centre, arms), each numbered,
  captioned as the hypercube unfolded.
- geometry-fact-voronoi-nature-001 — Seed dots with hand-drawn
  cell borders between neighbours; one cell shaded, labelled
  "closer to my seed".
- geometry-fact-wallpaper-17-001 — Four pattern tiles showing
  rotation, mirror and glide marks differently, and a counter
  "17 groups in total, no 18th".
- math-fact-benford-001 — Nine bars for first digits 1..9
  falling on a log curve: 30 percent down to under 5.
- math-fact-birthday23-001 — 23 person dots; all pair lines
  faint, one matching pair highlighted, "253 pairs" beneath.
- math-fact-central-limit-001 — Three lumpy histograms on the
  left flowing by arrows into one smooth bell curve.
- math-fact-countable-rationals-001 — A grid of fractions
  with a diagonal zig-zag enumeration path and numbers
  1,2,3... assigned along it.
- math-fact-harmonic-diverges-slow-001 — Shrinking bars
  1, 1/2, 1/3 ... above a cumulative sum curve that crawls
  past 1, 2, 3 without ever hurrying.
- math-fact-normal-body-001 — A bell curve; little person
  marks stand at centre (many) and tails (few), labelled
  height from many small causes.
- math-fact-pick-theorem-001 — A lattice polygon on a dot
  grid; interior dots filled solid, boundary dots ringed,
  with the two counts written out.
- math-fact-pigeonhole-socks-001 — Eleven bird dots above ten
  boxes; arrows land them and one box visibly gets two.
- math-fact-ramsey-friends-001 — Six nodes in a ring, every
  pair connected faintly; one triangle glows: friends or
  strangers, a trio is forced.
- math-fact-six-degrees-001 — A chain of person dots from
  "you" to "stranger": six hops drawn long above, four hops
  drawn shorter below (the platform-era measurement).
- math-fact-zipf-law-001 — Word bars: "the" full height,
  "of" half, "and" a third, trailing off; rank on the axis.
- ml-fact-alphazero-tabula-001 — A small chessboard with a
  circular self-play arrow around it; below, a "human
  openings" book crossed out and a rising strength curve.
- ml-fact-backprop-1986-001 — A timeline 1970-1990 with three
  flags: 1974 thesis, 1986 Nature paper, and "then it caught
  fire" as small network sparks after.
- ml-fact-batchnorm-landscape-001 — A wide shifted bell
  (activations before) arrowed into a centred narrow bell;
  a question mark over "covariate shift?" and a smooth hill
  icon for the real explanation.

## Batch N2 — network rest + first chains (25)

- ml-fact-curse-dimensionality-001 — Left: 2D dots at varied
  distances. Right: dots spread on a thin shell ring, all
  nearly the same distance from the centre.
- ml-fact-dqn-atari-001 — A Breakout screen (bricks, paddle,
  ball with a tunnel behind the wall) feeding pixels into a
  small network box; score counter rising.
- ml-fact-dropout-ensemble-001 — One network whose units
  flicker off in changing subsets; beneath, three thin
  "sub-network" copies and a vote into the full net.
- ml-fact-imagenet-moment-001 — Error bars 2010-2012 near
  26-28 percent, then AlexNet's bar dropping to 15.3 with
  two small GPU boxes beside it.
- ml-fact-moe-sparse-001 — A router diamond reading a token
  and lighting only 2 of 8 expert boxes; the rest stay dim,
  "pay for 2, own 8".
- ml-fact-pca-eigenfaces-001 — A face oval above a row of
  ghost component ovals; weight bars under each ghost sum
  back into the face.
- ml-fact-perceptron-hype-001 — A 1958 newspaper frame; inside,
  one neuron diagram and a speech bubble: "will walk, talk,
  see..." — the promise vs the circuit.
- ml-fact-random-forest-trees-001 — Three scraggly decision
  trees drop ballots into a majority box; the wrong solo
  ballot is outvoted.
- ml-fact-recommender-bubble-001 — A user dot before a wide
  funnel of varied items; the funnel narrows to three
  repeated sameness items circled as a bubble.
- ml-fact-self-attention-cost-001 — Token squares: four tokens
  with all pair lines (16), then eight tokens' corner of a
  much denser web, "cost grows as n squared".
- ml-fact-transformer-paper-001 — A row of tokens with arcs
  connecting every pair directly; below, a crossed-out
  chain link labelled "recurrence removed".
- ml-fact-xor-winter-001 — A 2x2 plot: filled dots on one
  diagonal, empty on the other, one straight line failing
  every way it tilts; "no single line separates XOR".
- programming-fact-ajax-gmail-001 — A page frame where only
  one panel refreshes with a spinner while the rest of the
  page stays put; a faint full-reload circular arrow crossed.
- programming-fact-eniac-programmers-001 — A wall panel of
  sockets in a grid with swooping patch cables plugged by
  six small operator dots along the bottom.
- programming-fact-erlang-nines-001 — Many tiny process
  circles; one bursts (X), a supervisor box above sends a
  restart arrow and a fresh circle appears.
- programming-fact-jit-hotspot-001 — Code blocks in a row;
  one glows as "hot: profiled 10,000 runs" and drops through
  a compiler funnel into native code.
- programming-fact-linus-hobby-001 — A terminal post: three
  quoted lines ("just a hobby..."), and beneath a small tree
  of contributors growing branches.
- programming-fact-mapreduce-paper-001 — Documents split into
  shards, map boxes emit key pairs, arrows shuffle them by
  key into reduce boxes adding totals.
- programming-fact-morris-worm-001 — Machine nodes in a ring;
  a worm dot travels and each visited node sprouts copies
  until the ring clogs.
- programming-fact-pagerank-eigen-001 — Web page nodes of
  different sizes joined by link arrows; the biggest node
  collects the most arrows, "rank flows along links".
- programming-fact-shannon-bit-001 — A relay switch circuit
  AND/OR drawn with contacts, and below a clean bit stream
  0 1 1 0 labelled "information, measured".
- programming-fact-simd-lanes-001 — One long register split
  into 16 lanes with numbers; a single instruction banner
  above applies "+" to all lanes at once.
- programming-fact-smalltalk-balloon-001 — Speech-bubble
  objects (a number, a window, a point) exchanging message
  arrows; even "3" is an object receiving "+ 4".
- architecture-fact-anycast-001 — A globe with three pins
  sharing one label "same IP"; a user arrow bends to the
  nearest pin only.
- architecture-fact-ashley-lessons-001 — Backup tapes on a
  shelf under a vault door; a restore-test lever rusted at
  "never tried", with a question mark over the tapes.

## Batch C1 — chains, part 1 (25)

- architecture-fact-aws-s3-typo-001 — A command line with one
  wrong character boxed; below, a row of server boxes where
  far more than intended grey out at once.
- architecture-fact-ba-power-2017-001 — A plug pulled from a
  power strip; datacenter blocks behind it go dark in
  sequence, then flicker wrongly on restart.
- architecture-fact-backpressure-001 — A pump on the left, a
  tank (queue) filling in the middle, and a return signal
  arrow telling the pump to slow before overflow.
- architecture-fact-bgp-pakistan-2008-001 — A globe; the route
  to a video pin bends away mid-ocean into another country's
  pin where it ends in an X.
- architecture-fact-blackout-alarm-2003-001 — A small power
  grid whose lines fail one by one; an alarm bell above with
  a slash through it, operators' desk empty.
- architecture-fact-blameless-postmortems-001 — An incident
  timeline board; a person icon shielded by a "no blame"
  badge while magnifying glasses point at system gears.
- architecture-fact-boeing-mcas-redundancy-001 — A plane
  profile; one sensor dot marked faulty feeding repeated
  nose-down arrows, a second ghost sensor beside it labelled
  "should compare".
- architecture-fact-bulkheads-001 — A ship hull in
  cross-section with watertight compartments; one floods
  dark, neighbours stay dry.
- architecture-fact-cap-partition-001 — Two islands after a
  cut cable: left answers with a "stale" tag, right shows a
  "refused" hand; scissors on the cut.
- architecture-fact-cdn-origin-pull-001 — A map: first request
  travels a long arrow to origin, the next three stop at the
  nearby edge pin.
- architecture-fact-circuit-breaker-001 — A wire with a switch
  that snaps open after three failure sparks; a timer ring
  shows the half-open probe.
- architecture-fact-cloudflare-regex-2019-001 — The pattern
  "(a+)+" above a branching tree that explodes in width; a
  CPU gauge needle pinned at max.
- architecture-fact-consistent-hashing-001 — A ring with
  server nodes; key dots sit with the next server clockwise;
  one new server lights and only its arc's keys move.
- architecture-fact-crowdstrike-2024-001 — One update file
  entering a globe of monitor squares; monitors flip to a
  crash X in a wave.
- architecture-fact-denver-baggage-001 — An airport track loop
  with suitcase squares tumbling at a junction; a calendar
  page labelled "+1 year" beside it.
- architecture-fact-dkim-spf-dmarc-001 — A big envelope with
  three stamp seals appearing in order: SPF, DKIM, DMARC.
- architecture-fact-dns-ttl-trade-001 — A record pin with a
  draining TTL bar and clock; low TTL refreshes fast, high
  TTL lingers stale.
- architecture-fact-dynamo-cart-001 — Two shopping carts with
  diverging items that merge by arrows into one cart neither
  shopper fully wrote.
- architecture-fact-email-store-forward-001 — An envelope
  hopping between relay towers; one tower sleeps (moon),
  the envelope waits in a queue tray, then continues.
- architecture-fact-equifax-struts-001 — A building facade of
  windows all shield-patched but one dark window, with a
  scanner beam finding it too late.
- architecture-fact-error-budgets-001 — A budget gauge
  draining coin dots as features ship; at zero a freeze lock
  closes over the rocket icon.
- architecture-fact-etag-revalidation-001 — Browser box
  holding a page and tag; it asks "same?" and receives a
  tiny "304" reply instead of the full page.
- architecture-fact-exactly-once-myth-001 — Two copies of one
  envelope approach a dedup gate; one passes, the duplicate
  is dropped into a bin.
- architecture-fact-facebook-bgp-2021-001 — A globe whose route
  lines fade out dashed; a door with a badge reader marked X
  in the foreground.
- architecture-fact-fastly-config-2021-001 — A customer toggle
  switch; flipping it wakes a sleeping bug icon inside a
  network of nodes that start failing outward.

## Batch C2 — chains, part 2 (25)

- audio-fact-sample-rate-001 — A sine wave with sample dots
  at just over twice its peak rate; a second dashed wave shows
  the alias that appears when sampling too slowly.
- physics-fact-venus-day-001 — Venus circle with a slow
  spinning arrow almost still, beside a full orbit arrow
  completed around the Sun dot: year finishes first.
- programming-fact-first-bug-001 — A relay panel grid; one
  cell holds a small moth shape (two wing arcs) taped beside
  the logbook line "first actual bug".
- programming-fact-year-2038-001 — A 32-bit counter strip of
  boxes filling toward the last cell, which flips to a minus
  sign and a calendar page "2038".
- programming-fact-ada-first-algorithm-001 — A paper sheet
  with a table of numbers (Bernoulli), gears of the Engine
  beside it never built, marked ghost outline.
- programming-fact-halting-problem-001 — A machine box feeding
  its own output back through a "will it halt?" oracle loop
  that ties itself in a knot arrow.
- programming-fact-apollo-1202-001 — A cockpit panel with
  alarm lamps 1201/1202 blinking, a priority queue of tasks,
  the guidance task highlighted kept, radar task dimmed.
- programming-fact-ariane5-overflow-001 — A number line: a
  64-bit long bar forced into a short 16-bit box, overflow
  spilling as X marks, rocket silhouette tilting.
- programming-fact-mars-orbiter-units-001 — Two rulers, lbf
  and N, measuring the same burn arrow; the trajectory curve
  bends too low into a planet arc.
- programming-fact-therac-race-001 — Two typists' keystroke
  timelines racing to a "ready" flag that lights before the
  magnet settings settle; beam icon.
- programming-fact-binary-search-overflow-001 — A sorted row
  of boxes; lo and hi pointers whose midpoint calculation
  wraps past the end, shown with a bending arrow.
- programming-fact-pentium-fdiv-001 — A division worked on
  paper: 4195835 / 3145727, the answer's tail digits crossed
  and replaced, a lookup table with one missing cell.
- programming-fact-manchester-baby-001 — A CRT grid of 32x32
  dots (store), one line glowing: the first program stored
  in the same memory as data.
- programming-fact-ada-lovelace-vision-001 — The Engine gear
  train on the left; on the right musical notes and weave
  pattern icons it "could" produce, in dashed vision bubbles.
- programming-fact-hopper-compiler-001 — English-like words
  box "ADD" arrow through a compiler gear into 0/1 machine
  code strip; "first compiler 1952".
- programming-fact-hamilton-software-001 — A rope of woven
  wires (core rope memory) beside code pages stacked to a
  person's height mark.
- programming-fact-turing-machine-paper-001 — An infinite
  tape strip with square cells, a read head, and a tiny state
  table; the tape extends with ellipsis both ways.
- programming-fact-berners-web-free-001 — A document with
  link arrows to other documents forming a web; a price tag
  showing 0 crossed royalty.
- programming-fact-tomlinson-at-001 — A mailbox address being
  typed: user, then the @ symbol enlarged, then host; two
  computer boxes on either side.
- programming-fact-git-ten-days-001 — A calendar strip of ten
  days, each with a commit dot growing a branching graph;
  "self-hosting" when the graph manages itself.
- programming-fact-python-name-001 — A snake curve forming
  the path, ending at a circus silhouette hat; code bracket
  "print()" beside, name crossed from snake to show.
- programming-fact-javascript-ten-days-001 — Ten calendar
  cells racing a sprint runner; a language box shipped with
  rough edges (cracked corner) still running today.
- programming-fact-y2k-two-digits-001 — Year digits "19" fixed
  + two rolling digits 99 -> 00, a calendar flipping and a
  clock confused arrow looping back.
- programming-fact-moores-law-observation-001 — A staircase
  doubling steps of transistor dots on a chip square, years
  1965-2020 along the axis, curve slowing at the end.
- programming-fact-sorting-lower-bound-001 — A decision tree
  branching for 3 elements with 6 leaves labelled as the 6
  orders; "at least log2(n!) questions".

## Batch C3 — chains, part 3 (25)

- programming-fact-quicksort-worst-001 — Already-sorted bars;
  the first-element pivot splits off one bar at a time,
  partitions shrink by one: a staircase of wasted splits.
- programming-fact-halting-in-practice-001 — A "perfect
  checker" box crossed out; below, three partial tools
  (types, tests, linter) each catching a slice of bugs.
- programming-fact-np-verifier-001 — Left: a huge faint maze
  of search; right: one proposed path drawn bold, checked
  quickly step by step with ticks.
- programming-fact-ackermann-001 — A table A(m,n) whose values
  explode across the row: 1, 3, 7, 61, then a tower arrow off
  the frame.
- programming-fact-latency-numbers-001 — Log-scale horizontal
  bars: L1, RAM, SSD, disk seek, cross-country packet, each
  labelled with its rough time.
- programming-fact-false-sharing-001 — One 64-byte cache line
  holding variables A and B; two cores keep invalidating each
  other's copy, ping-pong arrows.
- programming-fact-float-tenth-001 — 0.1 expanded as a
  repeating binary fraction; the sum line reads
  0.30000000000000004 with the stray 4 highlighted.
- programming-fact-nan-not-equal-001 — Two identical NaN boxes
  facing each other with a != sign and an X over the equals
  that IEEE intends.
- programming-fact-utf8-design-001 — Byte patterns stacked:
  0xxxxxxx ASCII, then 110/1110/11110 lead bytes with
  10xxxxxx continuations, ASCII row glowing as already valid.
- programming-fact-emoji-grapheme-001 — One family emoji glyph
  decomposed into person code points joined by ZWJ links,
  "1 grapheme, many code points".
- programming-fact-regex-backtracking-001 — "(a+)+$" above a
  string of a's ending in b; a branching tree of ways to split
  that doubles at each step.
- programming-fact-amdahl-law-001 — A speedup curve rising
  toward a dashed ceiling at 10x labelled "the serial 10%
  rules".
- programming-fact-endianness-origin-001 — An egg cracked from
  the big end and the little end (two factions), below byte
  orders 12 34 vs 34 12 in memory.
- programming-fact-bloom-filter-001 — A bit array; three hash
  arrows from item "cat" set three bits; query "dog" hits an
  unset bit: "definitely not here".
- programming-fact-hyperloglog-001 — A funnel of countless
  distinct cards into a tiny register box labelled "12 KB"
  estimating billions.
- programming-fact-euclid-still-001 — A remainder staircase:
  1071 = 2x462 + 147 ... down to gcd 21, on a scroll labelled
  c. 300 BC.
- programming-fact-inverse-sqrt-hack-001 — The hex constant
  0x5f3759df in a box, one Newton step arrow refining a rough
  guess curve to the true 1/sqrt(x).
- programming-fact-copy-on-write-001 — Parent and child arrows
  sharing the same page boxes; one writes, only that page
  duplicates and splits off.
- programming-fact-branch-prediction-001 — A pipeline fork:
  the CPU races down the guessed branch, a "wrong" flag
  flushes those boxes away.
- programming-fact-gc-vs-refcount-001 — Two objects pointing
  at each other in a cycle, counters stuck at 1, unreachable
  from roots: the leak island.
- programming-fact-turing-completeness-css-001 — A row of
  checkbox cells evolving downward like Rule 110, selectors
  as the rule arrows.
- programming-fact-stack-frames-001 — A stack of call frames
  growing downward toward a "memory" floor; the top frame
  labelled "one more call?"
- programming-fact-pipes-mcilroy-001 — Small tool boxes
  cat | grep | wc chained by pipe glyphs, data dots flowing
  through, "one stubborn suggestion, 1964".
- programming-fact-fortran-1957-001 — A hand-written formula
  X = A + B*C fed through a compiler box to machine code;
  a scientist icon freed from wiring diagrams.
- programming-fact-lisp-homoiconic-001 — The expression
  (+ 1 (* 2 3)) drawn as a tree that is simultaneously a
  nested list of boxes: code = data.

## Batch C4 — chains, part 4 (25)

- programming-fact-simula-classes-001 — Ship silhouettes at
  sea (simulation) morphing into class/object boxes with the
  same hull outline; Simula 1967.
- programming-fact-codd-relational-001 — Tangled pointer
  records on the left; clean tables with rows/keys on the
  right; one internal report between them, 1970.
- programming-fact-visicalc-killer-app-001 — A grid of cells,
  one value changing and dependent cells rippling updates;
  an Apple II outline under the sheet.
- programming-fact-alto-gui-001 — One 1973 machine outline
  containing three labelled gifts: window, mouse, Ethernet
  cable, radiating to later computers.
- programming-fact-mosaic-images-001 — A text-only page on the
  left; the same page with an image block inline on the
  right, a crowd arrow "the Web takes off".
- programming-fact-tcp-flag-day-001 — A calendar page
  1 Jan 1983 with a flag; left protocol NCP switches off,
  right TCP/IP switches on, network dots keep flowing.
- programming-fact-dns-hosts-file-001 — One huge HOSTS.TXT
  scroll buckling; it explodes into a tree of DNS servers
  each holding a page.
- programming-fact-first-domain-001 — A 1985 calendar and the
  address symbolics.com as the first entry in a newborn
  registry book; .com stamp.
- programming-fact-csp-hoare-001 — 1978 paper at left; arrows
  of time to goroutine/light threads fanning into channels
  in Go, message arrows between them.
- programming-fact-prolog-facts-001 — Facts listed
  (parent(tom,bob)...), a query box, the machine's proof
  tree growing downward to "yes".
- programming-fact-haskell-laziness-001 — Many dialect boxes
  on the left converging into one Haskell box; an infinite
  list drawn lazily, only first cells solid.
- programming-fact-regex-kleene-001 — Neuron net sketch
  (1951) transforming by arrow into the notation a*, the
  mathematics of nerve nets becoming regex.
- programming-fact-emoji-kurita-001 — A 12x12 pixel grid
  heart drawn chunky, a pager outline around it, 176 glyphs
  in a small wall, 1999.
- programming-fact-wikiwikiweb-001 — An airport shuttle bus
  labelled "wiki wiki = quick", arrow to a web page anyone
  can edit, pencil icon.
- programming-fact-json-crockford-001 — A big JavaScript
  object literal; the simple data core highlighted and
  lifted out as JSON, "a subset that won".
- programming-fact-rest-dissertation-001 — A thesis book
  (2000) with arrows to browser/address-bar concepts:
  resources, URLs, stateless; no protocol box anywhere.
- programming-fact-opensource-cathedral-001 — A cathedral
  (single architect plan) vs a bazaar of many stalls
  contributing patches, eyeballs icons "given enough
  eyeballs".
- programming-fact-netscape-open-001 — A browser box cracking
  open (source released 1998), a mozilla lizard silhouette
  emerging, arrow to foundation.
- programming-fact-skiplist-001 — Express lanes over a sorted
  list: towers of different heights, a search path hopping
  the top lane then dropping down.
- programming-fact-hash-tree-bins-001 — A bucket filling with
  chained entries past 8, then re-drawing itself as a small
  balanced tree (Java HashMap).
- programming-fact-array-vs-list-cache-001 — Array cells
  contiguous with a cache-line bracket fetched at once;
  linked nodes scattered with arrows chasing pointers slowly.
- programming-fact-union-find-almost-001 — Trees flattening:
  find() with path halving, the tree squashes almost flat;
  alpha(n) "practically constant".
- programming-fact-heap-array-tree-001 — Left a binary heap
  tree, right its exact array [16,14,10,8,7...], index arrows
  parent 2i children.
- programming-fact-reservoir-sampling-001 — A stream of items
  flowing past, a reservoir of k slots; item n swaps in with
  probability k/n, dice.
- programming-fact-majority-vote-001 — A stream of votes, one
  counter and one candidate name; mismatches decrement,
  matches increment (Boyer-Moore).

## Batch C5 — chains, part 5 (25)

- programming-fact-fisher-yates-001 — A row of cards; from
  the right end, the highlighted card swaps with a random
  earlier one, shuffled region grows.
- programming-fact-sieve-eratosthenes-001 — Number grid 2..30
  with multiples of 2,3,5 crossed in waves; primes stay lit.
- programming-fact-duffs-device-001 — A switch staircase
  falling through into loop iterations, cases stacked inside
  a do-while outline.
- programming-fact-wal-survival-001 — Diary (log) written
  first, then the database page; a crash bolt between them
  shows replay arrows.
- programming-fact-btree-width-001 — One disk page as a wide
  box holding many keys and many child pointers; depth only
  3-4 for millions.
- programming-fact-fork-exec-split-001 — A process splitting
  (fork) into a copy, then the copy's body replaced (exec)
  by a new program icon.
- programming-fact-zerocopy-sendfile-001 — File on disk arrow
  straight to network socket; the user program box bypassed
  with a dashed fading path through it.
- programming-fact-overcommit-001 — Many promise notes (virtual
  memory) stacked against a smaller pile of real RAM chips;
  most promises never called in.
- programming-fact-pagecache-invisible-001 — First read arrow
  goes to disk; second read arrow stops at a glowing cache
  layer in RAM.
- programming-fact-context-switch-cost-001 — Two thread ribbons
  alternating; each switch drops a toll: cache lines cooling
  from lit to dim.
- programming-fact-timer-interrupts-001 — A clock with tick
  marks interrupting a running task ribbon; scheduler hands
  the CPU round the circle.
- programming-fact-inode-no-name-001 — An inode box (data +
  metadata) with two directory entries (names) pointing to
  it; name tags outside the box.
- programming-fact-deleted-open-file-001 — A file entry
  crossed "deleted" while an open handle keeps the inode
  alive; it fades only when the handle closes.
- programming-fact-signals-coarse-001 — A doorbell button and
  a bell above a process; multiple presses merge to one
  ring: no payload envelope.
- programming-fact-everything-file-001 — Keyboard, disk,
  network, printer all drawn as identical file icons with
  read/write arrows.
- programming-fact-chmod-bits-001 — Nine bit cells rwxrwxrwx
  grouped in threes: owner/group/others; flipping bits
  lights the letters.
- programming-fact-init-systemd-001 — A tree of processes all
  rooted at PID 1; an orphan child arrow re-attaches to the
  root.
- programming-fact-apollo-rope-memory-001 — Woven wire grid
  through ferrite rings (core rope), a hand threading it;
  read-only by construction.
- programming-fact-voyager-memory-001 — A tiny memory bar
  labelled ~68 KB against a huge modern phone bar off-chart;
  a signal dot travelling far.
- programming-fact-tech-debt-metaphor-001 — A loan ledger:
  shipping fast now, interest payments as extra work later,
  principal repaid by refactoring (Ward Cunningham).
- programming-fact-rubber-duck-001 — A code listing on the
  left, speech lines toward a duck outline on the desk; the
  bug line lights as explained.
- programming-fact-heisenbug-001 — A bug icon under a
  magnifying glass that fades when the glass is over it,
  reappearing at the edge.
- programming-fact-worse-is-better-001 — Two columns: perfect-
  but-unfinished cathedral vs simple-shipped tool with users;
  the shipped one ticked.
- programming-fact-second-system-001 — First system lean box,
  second system bloated with every feature bauble, creaking;
  third lean again (Brooks).
- programming-fact-os360-lesson-001 — A schedule Gantt and a
  staffing curve: adding people to the late project moves
  the finish later (Brooks's law graph).

## Batch C6 — chains, part 6 (25)

- programming-fact-nine-women-001 — Nine figure icons and a
  one-month calendar crossed out; beside, one figure and a
  nine-month timeline: Brooks's pregnancy line.
- math-fact-point999-001 — A number line zooming: 0.9, 0.99,
  0.999 arrows converging onto the same point as 1, no gap.
- math-fact-montyhall-001 — Three doors; car icon behind one,
  host opens a goat door, switch arrow to the other closed
  door with tally "wins 2 of 3".
- math-fact-gabriel-horn-001 — The horn y=1/x spun long and
  thin; a paint bucket fills its finite volume, coating
  arrows run off its endless surface.
- math-fact-zeta-minus12-001 — Partial sums 1,3,6,10 climbing
  away; a tag "analytic continuation: -1/12" pinned beside,
  explicitly not a sum.
- math-fact-pi-355-113-001 — 355/113 as stacked fraction over
  pi's digits, matching digits 3.1415929 highlighted to six
  places.
- math-fact-e-interest-001 — Compounding bars: yearly,
  monthly, daily steps approaching a smooth curve capped at
  e = 2.718...
- math-fact-euclid-primes-001 — Primes 2,3,5,7,11 multiplied,
  +1; the new number's prime factor starred "not in the
  list".
- math-fact-hilbert-hotel-001 — An endless corridor of rooms
  1,2,3,...; every guest shifts one door right, room 1 frees
  for the newcomer.
- math-fact-cantor-bigger-001 — Rows of binary decimals; the
  diagonal cells flipped build a new row at the bottom,
  missing from the list.
- math-fact-godel-001 — A framed axiom system; inside it a
  statement card "this statement is unprovable here" with a
  circular arrow.
- math-fact-fourcolour-001 — A map of regions coloured with
  four swatches only; a computer monitor ticking checked
  cases beside it.
- math-fact-fermat358-001 — x^n+y^n=z^n on a book page, a
  tiny margin note "no room", and a timeline 1637 to 1995.
- math-fact-collatz-open-001 — The orbit of 27: jagged up-down
  path finally falling to 1; a proof cloud with "?" above.
- math-fact-konigsberg-001 — River with four land masses and
  seven bridge lines; beside it the same as graph dots,
  odd-degree dots ringed.
- math-fact-simpson-001 — Two small charts with rising lines
  per group; the combined chart's line falls: Simpson's
  reversal drawn honestly.
- math-fact-base-rate-001 — A 1000-person dot grid; about 10
  true positives lit, a larger false-positive cluster from
  the healthy: "positive" mostly wrong.
- math-fact-regression-mean-001 — Scatter of parent vs child
  height with diagonal and a flatter regression line;
  extremes pull toward the mean.
- math-fact-arrow-voting-001 — A checklist of fairness wishes
  with a Condorcet cycle A>B>C>A making one always fail;
  "no perfect rule (Arrow)".
- math-fact-ham-sandwich-001 — Two irregular sandwich blobs;
  one straight knife line halves both areas, equal halves
  labelled.
- math-fact-hairy-ball-001 — A sphere covered in tangent
  arrows flowing around, forced into one swirl point on top.
- math-fact-polya-walk-001 — Left: a 2D grid walk looping home;
  right: 3D axes walk drifting away, "may never return".
- math-fact-buffon-needle-001 — Floorboard strips with needles
  dropped at angles; crossing tally feeds an estimate
  pi ~ 3.14.
- math-fact-st-petersburg-001 — Coin-flip payout table
  doubling 2,4,8,16... expected value infinity arrow versus
  a small "what people pay" coin stack.
- math-fact-kaprekar6174-001 — Four-digit numbers (3524,
  3087...) funnel by sort-subtract steps into 6174, which
  maps to itself.

## Batch C7 — chains, part 7 (25)

- math-fact-taxicab1729-001 — 1729 in the centre as the sum
  of two cube stacks drawn two ways: 1^3+12^3 and 9^3+10^3.
- math-fact-paper-moon-001 — A paper strip folding; thickness
  doubling steps 1,2,4... rising past a Moon dot at fold 42.
- math-fact-chessboard-rice-001 — Chessboard corner squares
  with grain piles doubling until the last square holds a
  mountain silhouette.
- math-fact-rubik-states-001 — A cube net of coloured-ish
  (greyscale) stickers scrambled; the count 43 quintillion
  written as a long zero tail.
- math-fact-deck52-factorial-001 — A shuffled row of 52 card
  miniatures; "52!" versus atoms-in-universe bar far below.
- math-fact-googol-origin-001 — 1 followed by 100 zeros wrapped
  in rows; a child speech bubble "googol!" 1938.
- math-fact-mersenne-primes-001 — 2^p - 1 formula with p prime;
  a scroll of the largest known prime digits trailing off.
- math-fact-perfect-numbers-001 — 6, 28, 496 circles with divisor
  arcs summing to themselves, Mersenne primes paired beside.
- math-fact-sqrt2-irrational-001 — A unit square with diagonal
  labelled sqrt(2); a fraction p/q crossed out, Greek column.
- math-fact-golden-sunflower-001 — Seeds spiralling by 137.5
  degrees from centre, counted spiral arms.
- math-fact-twin-primes-001 — Prime number line with twin pairs
  (11,13), (17,19) ringed; the rings fade into "?" far right.
- math-fact-clt-coins-001 — Ten coins and their heads counts
  histogram already bell-shaped over many trials.
- math-fact-law-large-numbers-001 — Running average line wild
  at left, settling onto true-value dashed line; casino chip.
- math-fact-kelly-criterion-001 — Bankroll curves: bet all
  crashes to zero, Kelly fraction grows steadily.
- math-fact-gamblers-ruin-001 — A small bankroll random walk
  against a huge house wall; walk absorbed at zero.
- math-fact-martingale-myth-001 — Bets 1,2,4,8,16 doubling
  staircase hitting a table-limit ceiling and a deep loss.
- math-fact-graham-number-001 — Tower of exponent arrows
  3^^^^3 ... layers labelled g1, g2 ... g64, dwarfing a
  googolplex dot.
- math-fact-euler-identity-001 — e^{i pi} + 1 = 0 large, five
  constants each underlined with name tags.
- math-fact-i-rotation-001 — Complex plane: point 1 rotated
  by x i to i, to -1, to -i, circular arrow quarter turns.
- math-fact-fixed-point-coffee-001 — A coffee cup with swirling
  arrows, one centre dot perfectly still ringed.
- math-fact-antipodes-weather-001 — Earth sphere with two
  antipodal pins joined through centre; thermometer/wind
  values equal sign between (Borsuk-Ulam flavour).
- math-fact-condorcet-cycle-001 — Three candidates in a
  circular arrow A>B, B>C, C>A with voter ballots beneath.
- math-fact-nash-equilibrium-001 — A payoff grid with one cell
  ringed stable: neither arrow out improves alone.
- math-fact-prisoners-dilemma-001 — 2x2 payoff matrix; arrows
  from both to (defect, defect) though (silent, silent) pays
  both more.
- math-fact-minimax-vonneumann-001 — Rock-paper-scissors circle
  with a dice; "optimal = mix randomly" vs a predictable
  pattern exploited.

## Batch C8 — chains, part 8 (25)

- math-fact-monte-carlo-pi-001 — Random dots in a square,
  those inside the quarter circle lit; ratio x4 estimates pi.
- math-fact-birthday-attack-sqrt-001 — A scale 365 boxes but
  collision spark at only 23 people; sqrt curve.
- math-fact-expectation-linear-001 — Two interlocked dice/
  gears labelled X and Y; E[X+Y] = E[X]+E[Y] anyway.
- math-fact-coupon-collector-001 — Coupon slots filling;
  expected waits 1, 1/2 ... the last slot's bar as long as all.
- math-fact-riemann-open-001 — Complex plane with zeros on the
  critical line x=1/2 ringed; a million-dollar tag.
- math-fact-axiom-choice-banach-001 — One sphere split by
  dashed cuts reassembling into two spheres (Banach-Tarski).
- math-fact-well-ordering-shock-001 — A scattered set of dots
  being pulled into one single queue line by "choice".
- math-fact-intermediate-value-001 — A continuous path from
  below a river line to above; crossing point forced ringed.
- math-fact-cauchy-strange-001 — A jagged fractal-ish function
  (Weierstrass) zooming jagged at every scale.
- math-fact-countable-algebraic-001 — A countable list of
  algebraic numbers as tiny strip vs the vast real line.
- math-fact-liouville-first-001 — 0.110001000000000000000001...
  digit pattern with growing zero runs, built transcendental.
- math-fact-goldbach-open-001 — Even numbers 4..20 as sums of
  two prime dots; beyond them a proof "?" horizon.
- math-fact-catalan-miha-001 — Powers on a number line: 8 and 9
  adjacent ringed, all other powers spaced apart.
- math-fact-erdos-probabilistic-001 — Dice over a combinatorial
  object; "if a random one works with P>0, one exists".
- math-fact-sylvester-gallai-001 — Scattered points; all the
  lines through pairs, one line touching exactly two ringed.
- math-fact-no-ruler-compass-001 — A construction done with
  compass arcs only; the straightedge lying crossed aside.
- math-fact-squaring-circle-001 — Circle and a square of equal
  area ghosted; ruler/compass crossed when pi proved
  transcendental (1882).
- math-fact-transcendental-pi-e-001 — pi + e = ? a balance with
  two known weights and an unknown verdict tag.
- math-fact-chaitin-omega-001 — Binary expansion of Omega with
  bits as halting answers; a lock over later bits "knowable
  only finitely".
- math-fact-busy-beaver-001 — Tiny Turing machines table; steps
  explode 1, 6, 21, 107... then "unknown" for 5 states.
- physics-fact-muons-rain-001 — Mountain, muon streaks; clock
  beside dilated: most should decay, many arrive.
- physics-fact-hot-tea-mass-001 — Two cups on a scale, hot one
  tipped heavier by E=mc^2 caption, absurdly tiny delta.
- physics-fact-charged-battery-mass-001 — Battery outline full
  vs empty on scale pans, fuller side heavier by 10^-12 kg.
- physics-fact-landauer-001 — A bit cell erased to 0, heat
  arrow out labelled kT ln2 minimum.
- physics-fact-maxwell-demon-001 — A demon at a door between
  fast/slow molecules, its notebook filling until erasure
  costs the savings.

## Batch C9 — chains, part 9 (25)

- physics-fact-tunnelling-sun-001 — Two proton dots facing a
  barrier wall between them in the Sun's core; one ghosted
  through the wall (tunnelling) with spark of fusion.
- physics-fact-uncertainty-intrinsic-001 — A wave packet:
  narrow position spike with wide momentum wave, and the
  reverse pair beneath (Heisenberg trade-off).
- physics-fact-double-slit-single-001 — Electron dots arriving
  one by one on a screen, gradually forming interference
  bands; slit wall in middle.
- physics-fact-no-ftl-entangle-001 — Two entangled particles
  flying apart, measurement dice identical-looking random on
  both sides; a "message?" envelope crossed.
- physics-fact-schrodinger-cat-001 — A box with cat silhouette
  and a sign "a reductio ad absurdum, 1935" - the satire label.
- physics-fact-casimir-001 — Two parallel plates with fewer
  wave squiggles between than outside; arrows pushing inward.
- physics-fact-hawking-temp-001 — Big black hole cool blue-ish
  (greyscale dim) vs tiny one bright hot, temperature labels
  inverse to mass.
- physics-fact-dirac-positron-001 — Equation E = +/- mc^2 with
  the minus branch leading to a positron track curling in a
  chamber (1932 photo style).
- physics-fact-neutrino-rain-001 — A human silhouette with
  countless faint streaks passing through, Sun above.
- physics-fact-redshift-tower-001 — A tower; light wave rising
  with stretching wavelength, red-shifted (greyscale spacing)
  at top (Pound-Rebka).
- physics-fact-speedlimit-info-001 — Race track: light beam
  finish line, rocket, signal, causality cone; all capped.
- physics-fact-planck-scale-001 — Length ruler zooming down:
  atom, nucleus, then Planck length wall where QM and gravity
  icons collide.
- physics-fact-metre-light-001 — Light ray travelling for
  1/299792458 s bracket labelled "1 metre (since 1983)", old
  bar crossed.
- physics-fact-second-caesium-001 — Caesium atom with tick
  marks counting 9,192,631,770 oscillations = 1 s.
- physics-fact-kilogram-planck-001 — The old platinum cylinder
  crossed, replaced by h constant and a Kibble balance.
- physics-fact-absolute-zero-001 — Temperature staircase
  descending toward 0 K dashed floor, steps halve forever.
- physics-fact-alpha-137-001 — The number 1/137.035999... as a
  large inscription, Feynman quote tag "a mystery".
- physics-fact-proton-electron-1836-001 — Balance: one proton
  pan vs 1836 tiny electron dots on the other.
- physics-fact-equivalence-tested-001 — Feather vs hammer /
  two masses falling side by side in a satellite, deviation
  meter at 10^-15.
- physics-fact-day-lengthening-001 — Earth with Moon receding
  arrow; clock face 22h in dinosaur era vs 24h now.
- physics-fact-sky-blue-001 — Sun beam entering air with tiny
  molecules; blue-ish (light) short waves scattered everywhere,
  long waves pass straight.
- physics-fact-metal-cold-001 — Metal bar and wood block at
  same 20C label; heat arrows drain fast from finger into
  metal, slow into wood.
- physics-fact-glass-not-liquid-001 — Old window pane with
  uneven thickness at manufacture (blown crown) label; a
  horizontal "flow after 800 yrs: none" gauge.
- physics-fact-microwave-frequency-001 — Oven box, water
  molecule rotating arrows at 2.45 GHz, "not a resonance:
  just a good, allowed frequency".
- physics-fact-lightning-hot-001 — Lightning bolt with
  thermometer bursting past Sun-surface marker 30,000 K vs
  5,500 K.

## Batch C10 — chains, part 10 (25)

- physics-fact-static-shock-001 — Hand approaching a doorknob,
  spark gap; gauge showing ~10 kV but tiny charge (harmless).
- physics-fact-frog-levitation-001 — Magnet bore circle, a
  frog silhouette floating centre with diamagnetic arrows.
- physics-fact-superconductor-meissner-001 — A disc with field
  lines bending around it, a magnet hovering above.
- physics-fact-pressure-cooker-001 — Pot cross-section, sealed
  lid, thermometer rising past 100C to 120C as pressure builds.
- physics-fact-sweat-cooling-001 — Skin surface, water molecules
  escaping; fastest ones leave, average energy falls.
- physics-fact-boomerang-nebula-001 — Star with outflowing cone,
  thermometer at ~1 K against space 2.7 K.
- physics-fact-sun-sound-delay-001 — Sun blast icon, sound wave
  crawling along timeline vs light arriving in 8 minutes.
- physics-fact-escape-velocity-001 — Planet with trajectories:
  fall back, orbit ellipse, escape hyperbola at 11.2 km/s.
- physics-fact-coriolis-myth-001 — Two sinks draining both ways
  in both hemispheres, Earth Coriolis arrows dwarfed by tap
  geometry.
- physics-fact-cmb-temperature-001 — Early universe hot glow
  fading along timeline to a thermometer at 2.725 K, microwave
  sky.
- physics-fact-lightning-sprites-001 — Thundercloud with normal
  lightning down and red (bright) sprite jellyfish above toward
  space.
- physics-fact-volcano-cooling-001 — Volcano plume into
  stratosphere, aerosol veil around globe, temperature dip
  chart for years.
- physics-fact-sound-speed-water-001 — Two lanes, air vs water
  sound wavefronts, water front 4.4x ahead after 1 second.
- physics-fact-deep-ocean-pressure-001 — Ocean depth column,
  diver crushing gauge, "1 tonne per cm2 at 10 km".
- physics-fact-ice-floats-anomaly-001 — Water molecules lattice
  expanding on freezing; ice cube floating with 9/10 submerged.
- physics-fact-time-crystal-space-001 — Telescope receiving old
  light cone from early galaxy while Earth icon forms later;
  label about oldest light (time crystal renamed by theme).
- physics-fact-antimatter-banana-001 — Banana with rare positron
  spark every ~75 minutes, potassium-40 tag.
- architecture-fact-two-generals-001 — Two generals on hills,
  messenger crossing valley captured; infinite ack regress.
- architecture-fact-lamport-clocks-001 — Three process timelines
  with logical counters increasing on message arrows, no
  wall clocks.
- architecture-fact-thundering-herd-001 — Cache key expiring
  clock; crowd of request arrows stampeding to database.
- architecture-fact-paxos-simple-001 — Paper stack "Paxos Made
  Simple" with proposer/acceptor ballot rounds.
- architecture-fact-idempotency-keys-001 — Retry button pressed
  three times, same key header, server applies once.
- architecture-fact-lsm-vs-btree-001 — LSM: sequential write
  segments stacking; B-tree random writes, read arrows trade.
- architecture-fact-two-phase-commit-001 — Coordinator asking
  prepare, one participant silent, all locked waiting.
- architecture-fact-saga-compensate-001 — Booking chain flight+
  hotel+car; one fails, compensations run backwards.

## Batch C11 — chains, part 11 (25)

- architecture-fact-spanner-truetime-001 — Datacenter racks
  with atomic clock and GPS icons; uncertainty interval bar
  TrueTime.
- architecture-fact-snowflake-ids-001 — ID bits as segments:
  timestamp | machine | sequence; numbers rolling sorted.
- architecture-fact-uuid-collision-001 — Space of UUID dots
  vast arena, birthday gauge absurdly far; "hell freezes".
- architecture-fact-hyrums-law-001 — API surface as ice with
  users standing on every observable crack/behaviour.
- architecture-fact-prime-video-monolith-001 — Many tiny
  Lambda/step boxes collapsing into one monolith box, cost
  bar -90%.
- architecture-fact-knight-capital-001 — A dead feature flag
  switch reused, old zombie code rising; money counter
  plunging 45 min timeline.
- architecture-fact-gitlab-backup-001 — Five backup methods as
  five theatre masks/empty boxes during a restore attempt.
- architecture-fact-notpetya-maersk-001 — Network of infected
  domain controllers, one offline in Ghana spared, rebuild
  arrow.
- architecture-fact-ovh-fire-backup-001 — Burning datacenter
  and its "backup" in same building burning too vs offsite.
- architecture-fact-tsb-migration-001 — Big bang switch night:
  old bank off, new on, crowd of locked-out customers 1.9M.
- architecture-fact-google-calendar-2019-001 — Calendar grid
  with one outage cell and blast-radius rings expanding.
- architecture-fact-rogers-2022-001 — Canada map outline of
  tower icons all going dark from one update box.
- architecture-fact-nhs-wannacry-001 — Hospital cross icon,
  patch window unpatched, worm arrows, old XP screen.
- architecture-fact-heartbleed-lesson-001 — Heartbeat request
  asking 3 letters but claiming length 64k, server leaking
  memory contents.
- architecture-fact-log4shell-ubiquity-001 — Log line with
  ${jndi:...} string reaching out to attacker server; library
  in everything diagram.
- architecture-fact-solarwinds-build-001 — Build pipeline
  factory line: clean source in, trojan update out signed.
- architecture-fact-stuxnet-airgap-001 — Air-gapped centrifuge
  room, USB stick bridging the gap, centrifuge spin speeds.
- architecture-fact-yahoo-breach-scale-001 — Breach counter
  numbers revising upward 500M, 1B, 3B over announcements.
- architecture-fact-tcp-handshake-001 — Two machines exchanging
  SYN, SYN-ACK, ACK arrows numbered 1-2-3.
- architecture-fact-slow-start-001 — Congestion window steps
  doubling 1,2,4,8 packets then flattening at a knee.
- architecture-fact-nagle-delayed-ack-001 — Two polite waiters
  holding doors for each other: Nagle waits for data, ACK
  waits 40ms.
- architecture-fact-http2-headline-001 — Many streams braided
  on one connection; one lost packet blocks all stream heads.
- architecture-fact-tls13-rtt-001 — Handshake timelines TLS1.2
  2 round trips vs TLS1.3 1, obsolete ciphers crossed.
- architecture-fact-ntp-stratum-001 — Stratum pyramid: atomic
  clocks stratum 0/1 down to laptops stratum 3.
- architecture-fact-protobuf-numbers-001 — Schema fields with
  permanent numbers 1,2,3; renaming a field label while the
  number stays.
