# FACTS_REVIEW.md — Audit of the 500 fact cards' visuals

*Reviewer pass, 2026-11-01. Authoritative for the fact
visuals. The fact TEXTS are fine (see below); the visuals fail
as a system and must all be re-authored, one per fact.*

## Method

- All 500 facts run through `tools/test_game.py`: **500/500
  technically OK** (valid, render, never score).
- Structural analysis of every `scene` block.
- Previews rendered for all 500; contact sheets visually
  inspected across topics (architecture, geometry, math, ml,
  physics, programming spot-checks throughout).

## Verdict

| What was checked | Result |
| --- | --- |
| Fact texts | **Keep.** Titles hook, bodies teach, node labels tell each fact's own mini-story. |
| Fact visuals | **Redo all 500.** Three recycled compositions cover the entire catalogue: |

| Recycled composition | Facts |
| --- | ---: |
| Same 3-box chain diagram (n0 → n1 → n2), only labels change | 399 |
| Unlabeled network mesh (generic layers) | 52 |
| Unlabeled orbits (3–5 rings around a sun) | 46 |
| No scene at all | 3 |

That is the whole problem: **the picture does not depict the
fact.** Jupiter's storm, Banach–Tarski, muons, Neptune's
density and 494 others wear one of three costumes. Sometimes
the costume accidentally fits (an orbit scene under an actual
orbital fact) — it is still the shared template.

## The rule (owner's instruction, non-negotiable)

**One fact = one new visual, authored for that fact. Never
reuse a scene — not from another fact, not from the games.**
The visual must depict the fact's subject or mechanism: the
wave for a sampling fact, the two clocks for time dilation,
the kissing circles for a packing fact. If a reader covered
the text, the picture alone should hint at what the fact is
about.

How, concretely:

- A labeled diagram is fine **only when the fact really is a
  process**, and then its structure must be the fact's own
  (vary node count, shape, direction; label the real things,
  not a 3-step slogan chain in the standard triangle pose).
- For anything spatial/physical/mathematical, write a small
  Python module instead (`"type": "fact"`, `paint(cr, view)`,
  no answer) — waves, orbits with real relative periods,
  curves, tilings, distributions. See `AGENTS.md` for the
  paint contract; a fact module needs no `target_at`.
- Calm motion where the subject moves (the pane animates at
  60 fps); `view.colors` only; both themes.
- Per fact: `tools/test_game.py <file>` green, previews
  (dark+light) **looked at**, scene visibly depicts the
  subject. Commit per topic batch (25), note "visual: bespoke"
  in FACTS_INDEX.md as you go.

Start with the orbits/network groups (pure decoration), then
the 3-box chains. Worklist: every fact below, grouped by the
composition it wears today.

#### Current visual: chain-3 (3-box diagram) — 399 facts

| Fact | Topic | Title (the actual subject) |
| --- | --- | --- |
| architecture-fact-anycast-001 | architecture | The same IP address can live in a hundred cities |
| architecture-fact-ashley-lessons-001 | architecture | Backups that nobody tested are a hope, not a plan |
| architecture-fact-aws-s3-typo-001 | architecture | An AWS typo took down a chunk of the Internet |
| architecture-fact-ba-power-2017-001 | architecture | British Airways grounded itself by unplugging the IT |
| architecture-fact-backpressure-001 | architecture | Fast producers must be told to slow down |
| architecture-fact-bgp-pakistan-2008-001 | architecture | One country's attempt to block YouTube blocked it worldwide |
| architecture-fact-blackout-alarm-2003-001 | architecture | The 2003 blackout grew behind a silenced alarm |
| architecture-fact-blameless-postmortems-001 | architecture | Blameless postmortems exist because fear hides causes |
| architecture-fact-boeing-mcas-redundancy-001 | architecture | MCAS trusted one sensor; redundancy is an architecture |
| architecture-fact-bulkheads-001 | architecture | Ships' bulkheads became a software pattern |
| architecture-fact-cap-partition-001 | architecture | Under a network partition, you must pick a poison |
| architecture-fact-cdn-origin-pull-001 | architecture | The first visitor to a new city pays for everyone |
| architecture-fact-circuit-breaker-001 | architecture | Circuit breakers exist because retries can be an attack |
| architecture-fact-cloudflare-regex-2019-001 | architecture | One regex, deployed everywhere at once, CPU'd the planet |
| architecture-fact-consistent-hashing-001 | architecture | Consistent hashing moves only 1/n of keys when a node joins |
| architecture-fact-crowdstrike-2024-001 | architecture | A sensor update crashed millions of Windows machines |
| architecture-fact-denver-baggage-001 | architecture | Denver's airport was delayed by its own baggage system |
| architecture-fact-dkim-spf-dmarc-001 | architecture | Email authentication arrived decades after email |
| architecture-fact-dns-ttl-trade-001 | architecture | Every DNS record carries its own staleness budget |
| architecture-fact-dynamo-cart-001 | architecture | Amazon's cart chose 'always writable' over always consistent |
| architecture-fact-email-store-forward-001 | architecture | Email was built to survive machines being off |
| architecture-fact-equifax-struts-001 | architecture | Equifax was breached through a patched-elsewhere framework |
| architecture-fact-error-budgets-001 | architecture | Reliability becomes negotiable with an error budget |
| architecture-fact-etag-revalidation-001 | architecture | An ETag lets a browser ask 'still the same?' cheaply |
| architecture-fact-exactly-once-myth-001 | architecture | Exactly-once delivery is impossible; dedup is the trick |
| architecture-fact-facebook-bgp-2021-001 | architecture | Facebook's 2021 outage locked its own engineers out |
| architecture-fact-fastly-config-2021-001 | architecture | One customer's valid setting triggered a dormant global bug |
| architecture-fact-gitlab-backup-001 | architecture | GitLab deleted its database and found backups were theatre |
| architecture-fact-google-calendar-2019-001 | architecture | Even Google Calendar has a blast radius |
| architecture-fact-heartbleed-lesson-001 | architecture | Heartbleed was two missing lines in a heartbeat |
| architecture-fact-http2-headline-001 | architecture | HTTP/2 multiplexed everything onto one fragile pipe |
| architecture-fact-hyrums-law-001 | architecture | Every observable behaviour of your API becomes a contract |
| architecture-fact-idempotency-keys-001 | architecture | A good retry button is really an idempotency key |
| architecture-fact-keepalive-cost-001 | architecture | Connection reuse exists because handshakes are expensive |
| architecture-fact-knight-capital-001 | architecture | Knight Capital lost $440M in 45 minutes to a dead flag |
| architecture-fact-lamport-clocks-001 | architecture | Lamport ordered events without trusting any clock |
| architecture-fact-log4shell-ubiquity-001 | architecture | Log4Shell hid in a logging library's helpful feature |
| architecture-fact-lsm-vs-btree-001 | architecture | Write-heavy stores trade read work for write speed |
| architecture-fact-mqtt-qos-001 | architecture | MQTT's QoS 2 is a four-step handshake in miniature |
| architecture-fact-nagle-delayed-ack-001 | architecture | Two polite algorithms once made each other wait |
| architecture-fact-nhs-wannacry-001 | architecture | WannaCry hurt hospitals through unpatched known holes |
| architecture-fact-notpetya-maersk-001 | architecture | Maersk was saved by a domain controller that lost power |
| architecture-fact-ntp-stratum-001 | architecture | Internet time descends from atomic clocks in layers |
| architecture-fact-ovh-fire-backup-001 | architecture | Fire taught the difference between backup and replica |
| architecture-fact-paxos-simple-001 | architecture | Paxos was so hard to explain it needed a sequel paper |
| architecture-fact-prime-video-monolith-001 | architecture | Prime Video cut costs 90 percent by un-distributing a tool |
| architecture-fact-protobuf-numbers-001 | architecture | In protobuf, field numbers are forever; names are free |
| architecture-fact-range-resume-001 | architecture | Downloads resume because HTTP can ask for slices |
| architecture-fact-read-replica-lag-001 | architecture | Read replicas can honestly return yesterday's news |
| architecture-fact-rogers-2022-001 | architecture | One maintenance update silenced a national carrier |
| architecture-fact-saga-compensate-001 | architecture | Sagas undo work with new work, never by time travel |
| architecture-fact-sharding-hotspot-001 | architecture | Sharding by the wrong key creates one celebrity shard |
| architecture-fact-slow-start-001 | architecture | TCP begins every connection deliberately slow |
| architecture-fact-snowflake-ids-001 | architecture | Twitter's Snowflake IDs sort themselves by time |
| architecture-fact-solarwinds-build-001 | architecture | SolarWinds attackers compromised the build, not the product |
| architecture-fact-spanner-truetime-001 | architecture | Google put atomic clocks and GPS into its datacenters |
| architecture-fact-stuxnet-airgap-001 | architecture | Stuxnet crossed an air gap on a USB stick |
| architecture-fact-tcp-handshake-001 | architecture | TCP's three-way handshake proves both sides can hear |
| architecture-fact-thundering-herd-001 | architecture | When a hot cache entry expires, the database gets mobbed |
| architecture-fact-tls13-rtt-001 | architecture | TLS 1.3 deleted a round trip and some antiques |
| architecture-fact-tsb-migration-001 | architecture | TSB's big-bang migration locked out 1.9 million customers |
| architecture-fact-two-generals-001 | architecture | Two generals cannot agree over an unreliable messenger |
| architecture-fact-two-phase-commit-001 | architecture | Two-phase commit can block everyone on one coordinator |
| architecture-fact-uuid-collision-001 | architecture | Random UUIDs collide about when hell freezes over |
| architecture-fact-websocket-upgrade-001 | architecture | WebSockets begin life as an HTTP request in disguise |
| architecture-fact-yahoo-breach-scale-001 | architecture | Yahoo's breach grew every time it was recounted |
| audio-fact-a440-standard-001 | audio | Concert A became 440 Hz only in the twentieth century |
| audio-fact-aliasing-fold-001 | audio | Too-high notes fold into false low ones: aliasing |
| audio-fact-autotune-cher-001 | audio | Auto-Tune's famous warble was a setting, not an accident |
| audio-fact-cochlea-place-001 | audio | Your inner ear is a piano laid out in a spiral |
| audio-fact-deutsch-octave-001 | audio | The octave illusion puts sounds in the wrong ear |
| audio-fact-ears-emit-sound-001 | audio | Healthy ears emit faint sounds of their own |
| audio-fact-loudness-curves-001 | audio | Ears are not microphones: bass vanishes when quiet |
| audio-fact-loudness-war-001 | audio | Music got louder by getting dynamically poorer |
| audio-fact-missing-fundamental-001 | audio | Your phone plays bass notes it cannot physically make |
| audio-fact-mp3-masking-001 | audio | MP3 deletes sounds you would not have heard anyway |
| audio-fact-piano-stretch-001 | audio | Pianos are tuned deliberately out of tune |
| audio-fact-precedence-haas-001 | audio | The first sound to arrive owns the direction |
| audio-fact-room-modes-001 | audio | Small rooms boom at notes set by their walls |
| audio-fact-sabine-reverb-001 | audio | Reverb science began with seat cushions at night |
| audio-fact-shepard-tone-001 | audio | A tone can rise forever and never get higher |
| audio-fact-stradivarius-blind-001 | audio | Blindfolded players do not reliably pick Stradivari |
| audio-fact-theremin-touchless-001 | audio | The theremin is played without touching it |
| audio-fact-vocoder-war-001 | audio | The vocoder was built to shrink and secret speech |
| cloud-fact-az-correlated-001 | cloud | Availability zones fail together more often than brochures |
| cloud-fact-clock-skew-leases-001 | cloud | Cloud leases assume clocks lie a little |
| cloud-fact-cold-start-physics-001 | cloud | Serverless cold starts are mostly loading, not laziness |
| cloud-fact-data-gravity-001 | cloud | Data attracts applications the way mass attracts mass |
| cloud-fact-egress-asymmetry-001 | cloud | Clouds charge rent on the exit door, not the entrance |
| cloud-fact-fiber-light-speed-001 | cloud | Light in fiber goes about 200 km per millisecond |
| cloud-fact-latency-floor-001 | cloud | Geography sets a latency floor no provider can beat |
| cloud-fact-load-shedding-001 | cloud | Dropping some requests early saves the rest |
| cloud-fact-noisy-neighbor-001 | cloud | Your cloud neighbour can slow you without touching you |
| cloud-fact-retry-jitter-001 | cloud | Polite retries back off exponentially and roll dice |
| cloud-fact-s3-strong-2020-001 | cloud | Amazon S3 changed its consistency personality in 2020 |
| cloud-fact-snowmobile-exabyte-001 | cloud | AWS once sent an 18-wheeler to collect exabytes |
| cloud-fact-spot-markets-001 | cloud | Cloud spare capacity is sold like an airline seat market |
| cloud-fact-station-wagon-bandwidth-001 | cloud | Never underestimate a station wagon full of tapes |
| geometry-fact-antipodal-map-001 | geometry | Antipodal weather twins exist right now |
| geometry-fact-brachistochrone-001 | geometry | The fastest slide curve is a cycloid |
| geometry-fact-catenary-arch-001 | geometry | A hanging chain, flipped, is the perfect arch |
| geometry-fact-coastline-paradox-001 | geometry | Britain's coast has no definite length |
| geometry-fact-constant-width-body-001 | geometry | Constant-width solids that are not spheres |
| geometry-fact-cycloid-clock-001 | geometry | Huygens fixed clocks with cycloid cheeks |
| geometry-fact-desargues-shadow-001 | geometry | Two triangles, perspective from point and line |
| geometry-fact-descartes-circles-001 | geometry | Four kissing circles obey one tidy equation |
| geometry-fact-euler-formula-001 | geometry | Vertices minus edges plus faces equals two, almost always |
| geometry-fact-ford-circles-001 | geometry | Between two Ford circles hides an infinite family |
| geometry-fact-gerrymandering-geometry-001 | geometry | District shapes can be measured for mischief |
| geometry-fact-girih-tiles-001 | geometry | Medieval tilers may have beaten Penrose by 500 years |
| geometry-fact-hilbert-gis-001 | geometry | Hilbert curves order map tiles on disk |
| geometry-fact-involute-gears-001 | geometry | Gear teeth are shaped by unwinding string from a circle |
| geometry-fact-japanese-sangaku-lost-001 | geometry | Most sangaku tablets rotted away |
| geometry-fact-kissing-twelve-001 | geometry | Newton and Gregory argued over twelve or thirteen spheres |
| geometry-fact-koch-snowflake-001 | geometry | A snowflake can fence infinite perimeter around finite land |
| geometry-fact-morley-triangle-001 | geometry | Trisect every angle and an equilateral triangle appears |
| geometry-fact-napoleon-triangle-001 | geometry | Napoleon's theorem plants equilateral triangles everywhere |
| geometry-fact-pascal-hexagon-001 | geometry | Six points on a conic hide a straight line |
| geometry-fact-penrose-tiling-001 | geometry | Never-repeating tiles that conquered chemistry |
| geometry-fact-penrose-triangle-001 | geometry | The Penrose triangle exists in photographs, from one angle |
| geometry-fact-projective-perspective-001 | geometry | Painters invented projective geometry by looking |
| geometry-fact-reuleaux-drill-001 | geometry | A non-round triangle can drill a square hole |
| geometry-fact-sangaku-001 | geometry | Japanese temples hung geometry problems as offerings |
| geometry-fact-soddy-poem-001 | geometry | A geometry theorem was published as a love poem |
| geometry-fact-tractrix-pursuit-001 | geometry | Drag a watch on a chain: a tractrix |
| math-fact-antipodes-weather-001 | math | Right now, opposite sides of Earth share weather values |
| math-fact-arrow-voting-001 | math | No voting rule satisfies every fairness wish |
| math-fact-axiom-choice-banach-001 | math | Choice lets one ball become two, on paper |
| math-fact-base-rate-001 | math | A 99 percent accurate test can be mostly wrong |
| math-fact-birthday-attack-sqrt-001 | math | Collisions arrive at the square root, not halfway |
| math-fact-buffon-needle-001 | math | Dropping needles on floorboards estimates pi |
| math-fact-busy-beaver-001 | math | The busiest small machines outrun all comprehension |
| math-fact-cantor-bigger-001 | math | Some infinities are provably bigger than others |
| math-fact-catalan-miha-001 | math | 8 and 9 are the only consecutive perfect powers |
| math-fact-cauchy-strange-001 | math | There are functions continuous everywhere, tame nowhere |
| math-fact-chaitin-omega-001 | math | There is a number that encodes all of mathematics' secrets |
| math-fact-chessboard-rice-001 | math | The chessboard rice legend ends at a mountain of grain |
| math-fact-clt-coins-001 | math | Ten coins already hint at the bell curve |
| math-fact-collatz-open-001 | math | A problem a child can state has resisted everyone |
| math-fact-condorcet-cycle-001 | math | Majorities can prefer A to B, B to C, and C to A |
| math-fact-countable-algebraic-001 | math | Almost every real number is transcendental |
| math-fact-coupon-collector-001 | math | The last coupon takes as long as all the rest |
| math-fact-deck52-factorial-001 | math | Your shuffle has probably never happened before |
| math-fact-e-interest-001 | math | e was discovered by asking how interest compounds |
| math-fact-erdos-probabilistic-001 | math | Existence by dice: the probabilistic method |
| math-fact-euclid-primes-001 | math | Euclid proved primes never run out, in four lines |
| math-fact-euler-identity-001 | math | Euler's identity compresses five constants into one line |
| math-fact-expectation-linear-001 | math | Expectation adds even when variables conspire |
| math-fact-fermat358-001 | math | Fermat's margin note took 358 years to settle |
| math-fact-fixed-point-coffee-001 | math | Stirring coffee guarantees one unmoved point |
| math-fact-fourcolour-001 | math | The four colour theorem needed a computer's stamina |
| math-fact-gabriel-horn-001 | math | Finite paint fills it; infinite paint coats it |
| math-fact-gamblers-ruin-001 | math | Against a richer house, persistence is the trap |
| math-fact-godel-001 | math | Arithmetic hides true but unprovable statements |
| math-fact-goldbach-open-001 | math | Every even number tried is two primes; proof missing |
| math-fact-golden-sunflower-001 | math | Sunflowers pack seeds at the golden angle |
| math-fact-googol-origin-001 | math | A googol got its name from a nine-year-old |
| math-fact-graham-number-001 | math | Graham's number makes googolplex look like zero |
| math-fact-hairy-ball-001 | math | You cannot comb a hairy ball flat everywhere |
| math-fact-ham-sandwich-001 | math | One cut can halve two sandwiches exactly |
| math-fact-hilbert-hotel-001 | math | A full hotel with infinite rooms can still take guests |
| math-fact-i-rotation-001 | math | Multiplying by i is a quarter turn |
| math-fact-intermediate-value-001 | math | A continuous walk cannot jump over the riverbank |
| math-fact-kaprekar6174-001 | math | Every four-digit number falls into 6174 |
| math-fact-kelly-criterion-001 | math | Betting everything on an edge still ruins you |
| math-fact-konigsberg-001 | math | Seven bridges founded graph theory by being impossible |
| math-fact-law-large-numbers-001 | math | Casinos trust the law of large numbers, not luck |
| math-fact-liouville-first-001 | math | The first proven transcendental was built to be one |
| math-fact-martingale-myth-001 | math | Doubling bets cannot repeal arithmetic |
| math-fact-mersenne-primes-001 | math | The biggest known primes are almost all Mersenne |
| math-fact-minimax-vonneumann-001 | math | Optimal play in zero-sum games is often random |
| math-fact-monte-carlo-pi-001 | math | Randomness computes what geometry struggles with |
| math-fact-montyhall-001 | math | Switching doors wins the car twice as often |
| math-fact-nash-equilibrium-001 | math | Nash proved every finite game has a stable point |
| math-fact-no-ruler-compass-001 | math | A compass alone can do everything ruler-and-compass can |
| math-fact-paper-moon-001 | math | Fold paper 42 times and you pass the Moon |
| math-fact-perfect-numbers-001 | math | Perfect numbers and Mersenne primes are the same list |
| math-fact-pi-355-113-001 | math | 355/113 approximates pi to six decimal places |
| math-fact-point999-001 | math | 0.999... equals 1, exactly, not approximately |
| math-fact-polya-walk-001 | math | A random walker returns in 2D, may vanish in 3D |
| math-fact-prisoners-dilemma-001 | math | Individually rational, collectively foolish: the dilemma |
| math-fact-regression-mean-001 | math | Tall parents have shorter children, on average: regression |
| math-fact-riemann-open-001 | math | The Riemann hypothesis is a million-dollar pattern |
| math-fact-rubik-states-001 | math | A Rubik's cube has 43 quintillion positions |
| math-fact-simpson-001 | math | A trend can hold in every subgroup and reverse overall |
| math-fact-sqrt2-irrational-001 | math | The square root of 2 broke a Greek worldview |
| math-fact-squaring-circle-001 | math | Squaring the circle died when pi turned transcendental |
| math-fact-st-petersburg-001 | math | A coin game worth infinity that nobody will buy |
| math-fact-sylvester-gallai-001 | math | A line through exactly two points is guaranteed |
| math-fact-taxicab1729-001 | math | 1729 is the smallest number special in two ways |
| math-fact-transcendental-pi-e-001 | math | We do not know if pi + e is irrational |
| math-fact-twin-primes-open-001 | math | Twin primes are unproven after two thousand years |
| math-fact-well-ordering-shock-001 | math | Accept choice and every set can be lined up |
| math-fact-zeta-minus12-001 | math | 1+2+3+... = -1/12 is a label, not a sum |
| ml-fact-adversarial-examples-001 | ml | A panda plus invisible noise fools a network |
| ml-fact-alphafold-casp-001 | ml | AlphaFold2 essentially solved a 50-year grand challenge |
| ml-fact-bias-variance-001 | ml | Prediction error is a tug of war you cannot win twice |
| ml-fact-bpe-tokens-001 | ml | Language models read compression-born subwords |
| ml-fact-catastrophic-forgetting-001 | ml | Networks forget the old task acing the new |
| ml-fact-chinchilla-001 | ml | Famous models were trained on too little text |
| ml-fact-class-imbalance-accuracy-001 | ml | 99 percent accuracy can mean the model does nothing |
| ml-fact-cold-start-001 | ml | Recommenders are blind exactly when you are new |
| ml-fact-concept-drift-001 | ml | The world changes; yesterday's model is historical |
| ml-fact-data-leakage-target-001 | ml | Target leakage wins competitions and fails Mondays |
| ml-fact-decision-tree-entropy-001 | ml | Decision trees ask the question that splits doubt best |
| ml-fact-deepblue-brute-001 | ml | Deep Blue won with speed plus evaluation, not learning |
| ml-fact-distillation-001 | ml | A small model can be taught by a big one's hesitations |
| ml-fact-double-descent-001 | ml | Making a model bigger can make test error fall twice |
| ml-fact-eliza-effect-001 | ml | A 1966 keyword script convinced users it understood |
| ml-fact-embedding-bias-001 | ml | Word embeddings absorbed the stereotypes of their text |
| ml-fact-emergent-abilities-debate-001 | ml | 'Emergent abilities' may partly be a mirage of metrics |
| ml-fact-eval-contamination-001 | ml | Benchmarks leak into training data and inflate scores |
| ml-fact-feedback-loops-ml-001 | ml | Predictive policing can patrol its own predictions |
| ml-fact-gan-pub-001 | ml | GANs were argued into existence in a Montreal pub |
| ml-fact-gpt2-too-dangerous-001 | ml | GPT-2 was once staged-released as too dangerous |
| ml-fact-grokking-001 | ml | Networks can understand long after memorising |
| ml-fact-hallucination-mechanism-001 | ml | Hallucination is the training objective working as designed |
| ml-fact-human-feedback-cost-001 | ml | The humans in RLHF are an invisible workforce |
| ml-fact-imagenet-labels-001 | ml | ImageNet's secret ingredient was labelled data at scale |
| ml-fact-knn-simplicity-001 | ml | k-NN was analysed in 1967 and still embarrasses pipelines |
| ml-fact-label-errors-benchmark-001 | ml | Some benchmark labels are simply wrong |
| ml-fact-lottery-ticket-001 | ml | Big networks hide small networks that win alone |
| ml-fact-move37-001 | ml | Move 37 was first called a mistake by experts |
| ml-fact-naive-bayes-works-001 | ml | Naive Bayes lies about independence and often wins |
| ml-fact-no-free-lunch-ml-001 | ml | No algorithm is best at everything: that is a theorem |
| ml-fact-open-weights-irreversible-001 | ml | Released weights cannot be unreleased |
| ml-fact-positional-rope-001 | ml | Models know word order only because we inject it |
| ml-fact-pretraining-finetuning-001 | ml | Pretrain then fine-tune inverted who does the work |
| ml-fact-quantization-int8-001 | ml | Models survive rewriting in 8-bit integers |
| ml-fact-rlhf-preference-001 | ml | RLHF taught models manners from ranked preferences |
| ml-fact-scaling-laws-001 | ml | Language model quality follows eerily straight power laws |
| ml-fact-shortcut-learning-001 | ml | Models cheat with watermarks, rulers and backgrounds |
| ml-fact-spurious-texture-001 | ml | ImageNet networks judge by texture, not shape |
| ml-fact-svm-margin-001 | ml | Support vector machines care only about the borderline |
| ml-fact-temperature-sampling-001 | ml | Temperature: librarian or improviser knob |
| ml-fact-train-serving-skew-001 | ml | Models meet a different world than they trained in |
| ml-fact-turing-test-loebner-001 | ml | The Turing test measures judges as much as machines |
| ml-fact-watson-jeopardy-001 | ml | Watson won Jeopardy by ranking answers, not understanding |
| ml-fact-word2vec-arithmetic-001 | ml | king - man + woman lands near queen, unprogrammed |
| physics-fact-absolute-zero-001 | physics | Absolute zero is a limit you may approach, never reach |
| physics-fact-alpha-137-001 | physics | One dimensionless number in physics has no explanation |
| physics-fact-antimatter-banana-001 | physics | Bananas emit antimatter, at a homeopathic rate |
| physics-fact-boomerang-nebula-001 | physics | The coldest natural place is a star's outflow |
| physics-fact-casimir-001 | physics | Two empty plates attract because the vacuum is not nothing |
| physics-fact-charged-battery-mass-001 | physics | A charged battery weighs more than a dead one |
| physics-fact-cmb-temperature-001 | physics | The universe has a temperature: 2.725 kelvin |
| physics-fact-coriolis-myth-001 | physics | Toilet bowls do not reveal the hemisphere |
| physics-fact-day-lengthening-001 | physics | Days were about 22 hours when dinosaurs were young |
| physics-fact-deep-ocean-pressure-001 | physics | The deep ocean presses with a tonne per square centimetre |
| physics-fact-dirac-positron-001 | physics | Antimatter was found in an equation before a detector |
| physics-fact-double-slit-single-001 | physics | Single electrons build interference one dot at a time |
| physics-fact-equivalence-tested-001 | physics | Falling objects agree to 1 part in 10^15 |
| physics-fact-escape-velocity-001 | physics | Escape velocity is about not coming back, not about engines |
| physics-fact-frog-levitation-001 | physics | A live frog has floated in a magnet |
| physics-fact-glass-not-liquid-001 | physics | Old window panes are not slowly flowing glass |
| physics-fact-hawking-temp-001 | physics | Black holes have a temperature, and small ones are hot |
| physics-fact-hot-tea-mass-001 | physics | A hot cup of tea is heavier than the same tea cold |
| physics-fact-ice-floats-anomaly-001 | physics | Ice floats because water expands as it freezes |
| physics-fact-kilogram-planck-001 | physics | The kilogram is anchored to Planck's constant since 2019 |
| physics-fact-landauer-001 | physics | Erasing one bit must release a minimum of heat |
| physics-fact-lightning-hot-001 | physics | Lightning is several times hotter than the Sun's surface |
| physics-fact-lightning-sprites-001 | physics | Above thunderstorms, red sprites flash toward space |
| physics-fact-maxwell-demon-001 | physics | Maxwell's demon was defeated by its own memory |
| physics-fact-metal-cold-001 | physics | Metal feels colder than wood at the same temperature |
| physics-fact-metre-light-001 | physics | The metre is defined by light, not a bar |
| physics-fact-microwave-frequency-001 | physics | Microwaves heat food at 2.45 GHz, and not by resonance |
| physics-fact-muons-rain-001 | physics | Muons reach the ground by living in another time |
| physics-fact-neutrino-rain-001 | physics | Trillions of neutrinos pass through you every second |
| physics-fact-no-ftl-entangle-001 | physics | Entanglement cannot send messages, even in principle |
| physics-fact-planck-scale-001 | physics | Planck units mark where our two best theories collide |
| physics-fact-pressure-cooker-001 | physics | Pressure cookers cook by letting water get hotter |
| physics-fact-proton-electron-1836-001 | physics | One proton outweighs 1836 electrons |
| physics-fact-redshift-tower-001 | physics | Gravity reddens light climbing out of a basement |
| physics-fact-schrodinger-cat-001 | physics | Schroedinger's cat was an attack, not a proposal |
| physics-fact-second-caesium-001 | physics | One second is 9,192,631,770 ticks of caesium |
| physics-fact-sky-blue-001 | physics | The sky is blue because air itself scatters blue most |
| physics-fact-sound-speed-water-001 | physics | Sound travels about 4.4 times faster in water than air |
| physics-fact-speedlimit-info-001 | physics | Nothing carrying information outruns light in vacuum |
| physics-fact-static-shock-001 | physics | A doorknob shock is thousands of volts and harmless |
| physics-fact-sun-sound-delay-001 | physics | Sun storms would take a month to hear |
| physics-fact-superconductor-meissner-001 | physics | Superconductors expel magnetic fields |
| physics-fact-sweat-cooling-001 | physics | Sweat cools by taking the fastest molecules |
| physics-fact-time-crystal-space-001 | physics | The oldest light we see left before Earth existed |
| physics-fact-tunnelling-sun-001 | physics | The Sun shines by quantum tunnelling |
| physics-fact-uncertainty-intrinsic-001 | physics | Uncertainty is not clumsy measurement; it is the world |
| physics-fact-volcano-cooling-001 | physics | Big eruptions cool the planet for years |
| programming-fact-ackermann-001 | programming | The Ackermann function outruns every simple loop nest |
| programming-fact-ada-first-algorithm-001 | programming | The first algorithm ran only on paper |
| programming-fact-ada-lovelace-vision-001 | programming | Lovelace predicted computers would compose music |
| programming-fact-alto-gui-001 | programming | The GUI, mouse and Ethernet shared one 1973 machine |
| programming-fact-amdahl-law-001 | programming | Speeding up 90 percent of a program cannot give 10x forever |
| programming-fact-apollo-1202-001 | programming | Apollo 11 landed while its computer complained |
| programming-fact-apollo-rope-memory-001 | programming | Apollo's memory was woven by hand, literally |
| programming-fact-ariane5-overflow-001 | programming | Ariane 5 was lost to an overflowing number |
| programming-fact-array-vs-list-cache-001 | programming | Arrays beat linked lists on modern hardware by locality |
| programming-fact-berners-web-free-001 | programming | The Web was given away. That is why it won |
| programming-fact-binary-search-overflow-001 | programming | Binary search hid an overflow bug for years |
| programming-fact-bloom-filter-001 | programming | A Bloom filter can lie only in one direction |
| programming-fact-branch-prediction-001 | programming | Your CPU runs code that may never happen |
| programming-fact-btree-width-001 | programming | B-trees are wide because disks think in pages |
| programming-fact-chmod-bits-001 | programming | Unix permissions are three bits read three times |
| programming-fact-codd-relational-001 | programming | Databases were revolutionised by one internal report |
| programming-fact-context-switch-cost-001 | programming | Switching threads costs more than the switch |
| programming-fact-copy-on-write-001 | programming | Forking a process does not copy its memory |
| programming-fact-csp-hoare-001 | programming | Go's goroutines descend from a 1978 paper |
| programming-fact-deleted-open-file-001 | programming | A deleted Unix file lives until its last user lets go |
| programming-fact-dns-hosts-file-001 | programming | DNS exists because one text file stopped scaling |
| programming-fact-duffs-device-001 | programming | Duff's device interleaves a switch with a loop, legally |
| programming-fact-emoji-grapheme-001 | programming | One visible emoji can be many code points |
| programming-fact-emoji-kurita-001 | programming | Emoji were 12 by 12 pixels, designed for pagers |
| programming-fact-endianness-origin-001 | programming | Endianness is a Gulliver's Travels joke that stuck |
| programming-fact-euclid-still-001 | programming | The oldest algorithm still in textbooks is Euclid's |
| programming-fact-everything-file-001 | programming | 'Everything is a file' bent Unix toward uniformity |
| programming-fact-false-sharing-001 | programming | Two variables can be slow because they share 64 bytes |
| programming-fact-first-domain-001 | programming | The first .com was a computer maker's, in 1985 |
| programming-fact-fisher-yates-001 | programming | A fair shuffle swaps each card with a random earlier one |
| programming-fact-float-tenth-001 | programming | 0.1 + 0.2 is not 0.3, and binary is why |
| programming-fact-fork-exec-split-001 | programming | Unix split 'run a program' into two operations |
| programming-fact-fortran-1957-001 | programming | FORTRAN's promise: let scientists stop hand-coding machines |
| programming-fact-gc-vs-refcount-001 | programming | Reference counting cannot collect a cycle |
| programming-fact-git-ten-days-001 | programming | Git was written in weeks, out of necessity |
| programming-fact-halting-in-practice-001 | programming | Every linter works around an impossible perfect checker |
| programming-fact-halting-problem-001 | programming | No program can check all programs for halting |
| programming-fact-hamilton-software-001 | programming | Apollo software made failure a scheduling problem |
| programming-fact-hash-tree-bins-001 | programming | Java's hash maps turn crowded buckets into tiny trees |
| programming-fact-haskell-laziness-001 | programming | Lazy evaluation once united a fragmented field |
| programming-fact-heap-array-tree-001 | programming | A heap is a tree that lives inside an array |
| programming-fact-heisenbug-001 | programming | Some bugs vanish when you look at them: heisenbugs |
| programming-fact-hopper-compiler-001 | programming | Hopper built a compiler they said was impossible |
| programming-fact-hyperloglog-001 | programming | Billions of distinct items, counted in kilobytes |
| programming-fact-init-systemd-001 | programming | PID 1 has one job nobody else can do |
| programming-fact-inode-no-name-001 | programming | On Unix, a file's name is not part of the file |
| programming-fact-inverse-sqrt-hack-001 | programming | Quake's inverse square root used a magic hexadecimal number |
| programming-fact-javascript-ten-days-001 | programming | JavaScript was prototyped in about ten days |
| programming-fact-json-crockford-001 | programming | JSON won by being a subset of something else |
| programming-fact-latency-numbers-001 | programming | Memory is fast only next to a disk seek |
| programming-fact-lisp-homoiconic-001 | programming | In Lisp, code is its own data structure |
| programming-fact-majority-vote-001 | programming | One counter finds a majority without counting everything |
| programming-fact-manchester-baby-001 | programming | The first stored program ran 52 minutes, in 1948 |
| programming-fact-mars-orbiter-units-001 | programming | A Mars probe died over pounds vs newtons |
| programming-fact-moores-law-observation-001 | programming | Moore's law is an observation, not physics |
| programming-fact-mosaic-images-001 | programming | One browser feature made the Web popular: inline images |
| programming-fact-nan-not-equal-001 | programming | NaN is not equal to itself, on purpose |
| programming-fact-netscape-open-001 | programming | Mozilla was a codename before it was a foundation |
| programming-fact-nine-women-001 | programming | Nine women cannot make a baby in one month |
| programming-fact-np-verifier-001 | programming | NP is about checking, not solving |
| programming-fact-opensource-cathedral-001 | programming | The Cathedral and the Bazaar argued open code works better |
| programming-fact-os360-lesson-001 | programming | OS/360 taught the industry that schedules are not staffing |
| programming-fact-overcommit-001 | programming | Linux promises more memory than it has |
| programming-fact-pagecache-invisible-001 | programming | Your second read of a file usually never touches disk |
| programming-fact-pentium-fdiv-001 | programming | Intel once shipped a chip that divided wrongly |
| programming-fact-pipes-mcilroy-001 | programming | Unix pipes were one person's stubborn suggestion |
| programming-fact-prolog-facts-001 | programming | Prolog programs state facts; the machine finds the proof |
| programming-fact-python-name-001 | programming | Python is named after a comedy troupe |
| programming-fact-quicksort-worst-001 | programming | Quicksort's worst case hides in already-sorted input |
| programming-fact-regex-backtracking-001 | programming | A short regex can take longer than the age of the universe |
| programming-fact-regex-kleene-001 | programming | Regular expressions began as nerve-net mathematics |
| programming-fact-reservoir-sampling-001 | programming | You can sample fairly from a stream you cannot store |
| programming-fact-rest-dissertation-001 | programming | REST is a PhD thesis, not a protocol |
| programming-fact-rubber-duck-001 | programming | Programmers debug by explaining code to a duck |
| programming-fact-second-system-001 | programming | The second system is the most dangerous one you build |
| programming-fact-sieve-eratosthenes-001 | programming | A Greek sieve from 2300 years ago still finds primes |
| programming-fact-signals-coarse-001 | programming | Unix signals are a doorbell, not a message |
| programming-fact-simula-classes-001 | programming | Classes and objects were invented to simulate ships |
| programming-fact-skiplist-001 | programming | Skip lists balance themselves with coin flips |
| programming-fact-sorting-lower-bound-001 | programming | Comparison sorts cannot beat n log n, and it is provable |
| programming-fact-stack-frames-001 | programming | Recursion depth is limited by memory, not by the language |
| programming-fact-tcp-flag-day-001 | programming | The Internet once switched protocols on a deadline |
| programming-fact-tech-debt-metaphor-001 | programming | Technical debt was a metaphor about money, deliberately |
| programming-fact-therac-race-001 | programming | Therac-25: a race condition in a radiation machine |
| programming-fact-timer-interrupts-001 | programming | Multitasking exists because a clock keeps interrupting |
| programming-fact-tomlinson-at-001 | programming | Email's @ came from a rarely used key |
| programming-fact-turing-completeness-css-001 | programming | CSS plus HTML was shown to be Turing complete |
| programming-fact-turing-machine-paper-001 | programming | Computability came from an imaginary machine |
| programming-fact-union-find-almost-001 | programming | Union-find is constant for all practical purposes |
| programming-fact-utf8-design-001 | programming | UTF-8 was designed so ASCII is already valid UTF-8 |
| programming-fact-visicalc-killer-app-001 | programming | The spreadsheet was the first killer app |
| programming-fact-voyager-memory-001 | programming | Voyager's computers remember less than a car key fob |
| programming-fact-wal-survival-001 | programming | Databases survive crashes by writing the diary first |
| programming-fact-wikiwikiweb-001 | programming | The first wiki was named after a Honolulu bus |
| programming-fact-worse-is-better-001 | programming | Worse is better: the philosophy that shipped Unix and C |
| programming-fact-y2k-two-digits-001 | programming | Y2K was a memory-saving decision coming due |
| programming-fact-year-2038-001 | programming | The 2038 bug is a clock overflow, not a prophecy |
| programming-fact-zerocopy-sendfile-001 | programming | Sending a file need not pass through your program |
| security-fact-beyondcorp-aurora-001 | security | Google rebuilt access after being breached in 2009 |
| security-fact-code-is-speech-001 | security | A court fight made source code legally speech |
| security-fact-correct-horse-entropy-001 | security | Four random words beat one tortured password |
| security-fact-krack-wpa2-001 | security | KRACK made WPA2 handshakes replay their keys away |
| security-fact-navajo-code-001 | security | The Navajo code was never broken, and it was two codes deep |
| security-fact-nist-password-reversal-001 | security | The password rules' author publicly recanted them |
| security-fact-passkeys-origin-001 | security | Passkeys stop phishing by refusing the wrong site |
| security-fact-rowhammer-001 | security | Reading your own memory can flip bits in your neighbour's |
| security-fact-spectre-lesson-001 | security | Spectre made CPUs leak through their own predictions |
| security-fact-sql-injection-shape-001 | security | SQL injection is a grammar confusion, not bad luck |
| security-fact-timing-side-channel-001 | security | Passwords have been stolen by measuring nanoseconds |
| security-fact-totp-window-001 | security | Your 6-digit code is a clock, shared with the server |
| security-fact-van-eck-001 | security | A monitor's picture was recoverable from its radio leakage |
| security-fact-venona-reuse-001 | security | One-time pads failed the Soviets only when reused |
| security-fact-wep-iv-reuse-001 | security | WEP died because its 24-bit IVs repeated by lunch |

#### Current visual: orbits-3 — 18 facts

| Fact | Topic | Title (the actual subject) |
| --- | --- | --- |
| geometry-fact-great-circle-flights-001 | geometry | Planes to Tokyo fly toward the pole because Earth is round |
| geometry-fact-klein-bottle-001 | geometry | A Klein bottle has no inside; models fake one |
| geometry-fact-mobius-cut-001 | geometry | Cut a Möbius strip: you do not get two strips |
| geometry-fact-sphere-area-lune-001 | geometry | Sphere lunes have area by pure proportion |
| geometry-fact-spherical-triangle-001 | geometry | On a sphere, a triangle can have 3 right angles |
| geometry-fact-torus-donut-001 | geometry | Topologically, a coffee cup is a donut |
| physics-fact-chandrasekhar-001 | physics | A star's death has a weight limit of 1.4 Suns |
| physics-fact-earth-core-hot-001 | physics | Earth's core is as hot as the Sun's surface |
| physics-fact-great-red-spot-001 | physics | Jupiter's storm is wider than Earth and centuries old |
| physics-fact-hafele-keating-001 | physics | In 1971, clocks flown around the world disagreed on return |
| physics-fact-io-volcanic-001 | physics | Io kneads itself into the most volcanic body known |
| physics-fact-iss-falling-001 | physics | Astronauts float because they never stop falling |
| physics-fact-mars-olympus-001 | physics | Olympus Mons is nearly three Everests, and gently sloped |
| physics-fact-neutron-star-density-001 | physics | A neutron star packs a mountain range into a sugar cube |
| physics-fact-ocean-tides-two-001 | physics | There are two high tides because water bulges twice |
| physics-fact-sun-fate-white-dwarf-001 | physics | The Sun will end as a white dwarf, quietly |
| physics-fact-tidal-locking-001 | physics | The Moon was once much closer and days much shorter |
| physics-fact-venus-retrograde-001 | physics | Venus spins backwards, and nobody fully knows why |

#### Current visual: orbits-4 — 20 facts

| Fact | Topic | Title (the actual subject) |
| --- | --- | --- |
| geometry-fact-mercator-greenland-001 | geometry | Mercator makes Greenland look Africa-sized |
| geometry-fact-no-perfect-map-001 | geometry | A perfect flat map is a theorem-level impossibility |
| geometry-fact-winkel-tripel-001 | geometry | The atlas map is a three-way compromise |
| physics-fact-aurora-sound-001 | physics | Auroras are Earth's magnetic shield made visible |
| physics-fact-continental-drift-rejected-001 | physics | Wegener was right about continents, wrong about forces |
| physics-fact-dark-matter-rotation-001 | physics | Galaxies spin too fast for the stars we see |
| physics-fact-diamond-rain-001 | physics | It may rain diamonds inside Neptune and Uranus |
| physics-fact-earth-rotation-speed-001 | physics | You are moving at 1,600 km/h and feel nothing |
| physics-fact-eddington-eclipse-001 | physics | A 1919 eclipse made Einstein famous overnight |
| physics-fact-fusion-pp-chain-001 | physics | Sunlight began as gamma rays a hundred millennia ago |
| physics-fact-gps-relativity-001 | physics | GPS works only because relativity is corrected daily |
| physics-fact-gravitational-waves-2015-001 | physics | In 2015 we heard two black holes collide |
| physics-fact-great-oxidation-001 | physics | Oxygen was once a planetary poison gas |
| physics-fact-magnetic-reversals-001 | physics | Earth's magnetic poles have flipped hundreds of times |
| physics-fact-mercury-perihelion-001 | physics | Mercury's orbit misbehaved until gravity was rethought |
| physics-fact-milankovitch-001 | physics | Ice ages keep time with wobbles in Earth's orbit |
| physics-fact-moon-receding-001 | physics | The Moon drifts away about 4 centimetres a year |
| physics-fact-pulsar-clocks-001 | physics | Some pulsars keep time rivaling atomic clocks |
| physics-fact-saturn-floats-001 | physics | Saturn would float, in a large enough bathtub |
| physics-fact-seismic-shadow-001 | physics | Earth's liquid core was found by an earthquake shadow |

#### Current visual: orbits-5 — 8 facts

| Fact | Topic | Title (the actual subject) |
| --- | --- | --- |
| geometry-fact-bernoulli-spiral-tomb-001 | geometry | Bernoulli's tombstone got the wrong spiral |
| geometry-fact-dymaxion-map-001 | geometry | Fuller's map unfolds Earth into triangles |
| geometry-fact-geodesic-domes-001 | geometry | Fuller's domes get stronger as they get bigger |
| geometry-fact-loxodrome-spiral-001 | geometry | A fixed compass course spirals to the pole |
| geometry-fact-pentagon-soccer-001 | geometry | Every soccer ball hides exactly twelve pentagons |
| physics-fact-cmb-pigeons-001 | physics | The Big Bang's afterglow was found as antenna noise |
| physics-fact-olbers-dark-001 | physics | The night sky is dark because the universe has a birthday |
| physics-fact-snowball-earth-001 | physics | Earth may once have frozen nearly to the equator |

#### Current visual: network mesh — 52 facts

| Fact | Topic | Title (the actual subject) |
| --- | --- | --- |
| architecture-fact-byzantine-third-001 | architecture | Tolerating traitors takes more than triple the traitors |
| architecture-fact-chaos-monkey-001 | architecture | Netflix breaks its own production on weekdays, on purpose |
| architecture-fact-gossip-spread-001 | architecture | Cluster gossip spreads news like a rumour, on purpose |
| architecture-fact-grpc-streaming-001 | architecture | gRPC streams because one request-response rarely fits |
| audio-fact-dithering-paradox-001 | audio | Adding noise can make digital audio more accurate |
| cloud-fact-cell-based-001 | cloud | Amazon confines failures by building in cells |
| geometry-fact-five-platonics-001 | geometry | Exactly five perfect solids exist; Euclid ends there |
| geometry-fact-honeycomb-hales-001 | geometry | Bees were proved optimal only in 1999 |
| geometry-fact-kepler-oranges-001 | geometry | Greengrocers stack oranges the provably best way |
| geometry-fact-menger-sponge-001 | geometry | A sponge with zero volume, infinite surface |
| geometry-fact-peano-curve-001 | geometry | One curve can fill an entire square |
| geometry-fact-sphere-packing-dim8-001 | geometry | Sphere packing in 8D fell to a short proof |
| geometry-fact-tesseract-net-001 | geometry | A hypercube unfolds into eight cubes |
| geometry-fact-voronoi-nature-001 | geometry | Voronoi cells grow in giraffes, mud and dragonfly wings |
| geometry-fact-wallpaper-17-001 | geometry | Every wallpaper uses one of 17 symmetries |
| math-fact-benford-001 | math | Real data starts with 1 far more often than with 9 |
| math-fact-birthday23-001 | math | 23 strangers likely share a birthday |
| math-fact-central-limit-001 | math | Averages become bell-shaped almost regardless |
| math-fact-countable-rationals-001 | math | Fractions are countable; reals are not |
| math-fact-harmonic-diverges-slow-001 | math | The harmonic series diverges, but at a crawl |
| math-fact-normal-body-001 | math | Height is normal because many small causes add |
| math-fact-pick-theorem-001 | math | Farm plots on graph paper yield area by counting dots |
| math-fact-pigeonhole-socks-001 | math | Eleven pigeons, ten holes: the deepest trivial theorem |
| math-fact-ramsey-friends-001 | math | In any six people, three mutual friends or strangers |
| math-fact-six-degrees-001 | math | Six degrees shrank in the network era |
| math-fact-zipf-law-001 | math | In any book, the second word bows to the first |
| ml-fact-alphazero-tabula-001 | ml | AlphaZero taught itself chess, then crushed Stockfish |
| ml-fact-backprop-1986-001 | ml | Backpropagation was discovered at least three times |
| ml-fact-batchnorm-landscape-001 | ml | Batch norm works, maybe not for the stated reason |
| ml-fact-curse-dimensionality-001 | ml | In high dimensions, everything is far from everything |
| ml-fact-dqn-atari-001 | ml | One algorithm learned Atari from pixels |
| ml-fact-dropout-ensemble-001 | ml | Dropout is secretly an ensemble of countless networks |
| ml-fact-imagenet-moment-001 | ml | AlexNet won by 10 points and ended an era overnight |
| ml-fact-moe-sparse-001 | ml | Mixture of experts lets a model be big and cheap at once |
| ml-fact-pca-eigenfaces-001 | ml | Faces compress into ghostly averages called eigenfaces |
| ml-fact-perceptron-hype-001 | ml | The 1958 perceptron was promised to walk and talk |
| ml-fact-random-forest-trees-001 | ml | A forest of bad trees outvotes a single good one |
| ml-fact-recommender-bubble-001 | ml | Recommenders optimise engagement, not your future taste |
| ml-fact-self-attention-cost-001 | ml | Attention's power bill grows with the square of length |
| ml-fact-transformer-paper-001 | ml | 'Attention Is All You Need deleted recurrence |
| ml-fact-xor-winter-001 | ml | One XOR problem helped freeze AI research for years |
| programming-fact-ajax-gmail-001 | programming | Web apps became real when pages stopped reloading |
| programming-fact-eniac-programmers-001 | programming | ENIAC was programmed by rewiring it |
| programming-fact-erlang-nines-001 | programming | Erlang was built so phone switches basically never stop |
| programming-fact-jit-hotspot-001 | programming | JIT compilers optimise the code you actually run |
| programming-fact-linus-hobby-001 | programming | Linux began as 'just a hobby' |
| programming-fact-mapreduce-paper-001 | programming | MapReduce taught clusters by hiding the hard parts |
| programming-fact-morris-worm-001 | programming | The first Internet worm was a survey that escaped |
| programming-fact-pagerank-eigen-001 | programming | Google began as an eigenvector problem |
| programming-fact-shannon-bit-001 | programming | Shannon founded information theory and digital logic |
| programming-fact-simd-lanes-001 | programming | One instruction can do sixteen additions at once |
| programming-fact-smalltalk-balloon-001 | programming | Smalltalk hid an entire computer inside every object |

#### Current visual: NO SCENE — 3 facts

| Fact | Topic | Title (the actual subject) |
| --- | --- | --- |
| audio-fact-sample-rate-001 | audio | Why CDs sample at 44.1 kHz |
| physics-fact-venus-day-001 | physics | A Venusian day outlasts its year |
| programming-fact-first-bug-001 | programming | The first bug was not the first bug |