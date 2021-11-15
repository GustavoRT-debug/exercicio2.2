
from mininet.node import Topo
class myTopo( Topo ):
    def __init__(self):
        
        Topo.__init__(self)
        # Add hosts and switches
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        # Add links
        self.addLink( h1, s1)
        self.addLink( h2, s1)
        self.addLink( h6, s2)
        self.addLink( h5, s2)
        self.addLink( h3, s3)
        self.addLink( h4, s3)
        self.addLink( s1, s2)
        self.addLink( s2, s3)
       

topos = {'exercicio2': (lambda : Exercicio2())}
