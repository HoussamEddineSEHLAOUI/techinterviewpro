import simpy


def arrivee(env, serveur, tempsArrivee):
    i = 0
    while True:
        print('Client %d arrive à %d' % (i, env.now))
    env.process(finService(env, i, serveur, 20))
    yield env.timeout(tempsArrivee)
    i += 1


def finService(env, i, serveur, tempsService):
    # demande d'un serveur
    print('Client %d demande le service à %d' % (i, env.now))
    with serveur.request() as req:
        yield req
    # servir le client
    print('Client %d commence le service à %d' % (i, env.now))
    yield env.timeout(tempsService)
    print('Client %d termine le service à %d' % (i, env.now))

env = simpy.Environment()
serveur = simpy.Resource(env, capacity=2)
env.process(arrivee(env,serveur,15))
env.run(until=70)