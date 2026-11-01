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
