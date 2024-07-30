import numpy as np
from dwave.system import EmbeddingComposite, DWaveSampler, LeapHybridSampler
from dimod.core.sampler import Sampler
from dimod.reference.samplers.identity_sampler import IdentitySampler
import dimod

# QUBO
# P = 11 + 2.7x - 3y + 9.3xy
Q = {('x','x'): 2.7,
     ('y','y'): -3.0,
     ('x','y'): 9.3}
 

sampler=LeapHybridSampler()
sample_set=sampler.sample_qubo(Q)
samples = sample_set.samples()

print(samples[0])

