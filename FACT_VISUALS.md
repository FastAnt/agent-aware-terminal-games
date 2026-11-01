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
