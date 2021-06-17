#!/usr/bin/env python

" Custom Topology to use ONOS Controller"

from mininet.topo import Topo
from mininet.log import setLogLevel, info

class MyTopo( Topo ):

    def addSwitch(self, name, **opts ):
        kwargs = { 'protocols' : 'OpenFlow13'}
        kwargs.update( opts )
        return super(MyTopo, self).addSwitch( name, **kwargs )

    def __init__( self ):
        "Create MyTopo topology..."
        
        # Inisialisasi Topology
        Topo.__init__( self )

        # Tambahkan node, switch, dan host

        info( '*** Add switches\n')
        s1 = self.addSwitch('Banda Aceh')
        s2 = self.addSwitch('Medan')
        s3 = self.addSwitch('Pekanbaru')
        s4 = self.addSwitch('Jambi')
        s5 = self.addSwitch('Padang')
        s6 = self.addSwitch('Palembang')
        s7 = self.addSwitch('Bengkulu')
        s8 = self.addSwitch('Bandar Lampung')
        s9 = self.addSwitch('Serang')
        s10 = self.addSwitch('Jkt-UT')
        s11 = self.addSwitch('Jkt-UI')
        s12 = self.addSwitch('Jkt-DIKTI')
        s13 = self.addSwitch('Bandung')
        s14 = self.addSwitch('Semarang')
        s15 = self.addSwitch('Jogja')
        s16 = self.addSwitch('Surabaya')
        s17 = self.addSwitch('Malang')
        s18 = self.addSwitch('Denpasar')
        s19 = self.addSwitch('Mataram')
        s20 = self.addSwitch('Pontianak')
        s21 = self.addSwitch('Samarinda')
        s22 = self.addSwitch('Mrt')
        s23 = self.addSwitch('Palangkaraya')
        s24 = self.addSwitch('Makasar')
        s25 = self.addSwitch('Kendari')
        s26 = self.addSwitch('Palu')
        s27 = self.addSwitch('Gorontalo')
        s28 = self.addSwitch('Manado')
        s29 = self.addSwitch('Ambon')
        s30 = self.addSwitch('Ternate')
        s31 = self.addSwitch('Tual')
        s32 = self.addSwitch('Kupang')
        s33 = self.addSwitch('Manukwari')
        s34 = self.addSwitch('Jayapura')


        info( '*** Add hosts\n')
        h1 = self.addHost('Unimed', ip='10.1.0.1')
        h2 = self.addHost('Lhoks-Unimal', ip='10.1.0.2')
        h3 = self.addHost('Pdg-UNP', ip='10.2.0.3')
        h4 = self.addHost('Pyk-Politani', ip='10.2.0.5')
        h5 = self.addHost('Pdg-STSI', ip='10.1.0.4')
        h6 = self.addHost('Batam', ip='10.1.0.9')
        h7 = self.addHost('SuLiat-UBB', ip='10.1.0.8')
        h8 = self.addHost('PolSri', ip='10.1.0.7')
        h9 = self.addHost('21Bogor', ip='10.2.0.1')
        h22 = self.addHost('22Bogor', ip='10.2.0.2')
        h10 = self.addHost('Unpad', ip='10.2.0.3')
        h11 = self.addHost('Purwokerto', ip='10.2.0.4')
        h12 = self.addHost('Solo', ip='10.2.0.5')
        h13 = self.addHost('Unesa', ip='10.2.0.6')
        h14 = self.addHost('Jember', ip='10.2.0.7')
        h15 = self.addHost('Bangkalan', ip='10.2.0.8')
        h16 = self.addHost('ISI.Dps', ip='10.2.0.9')
        h17 = self.addHost('Singaraja', ip='10.3.0.1')
        h18 = self.addHost('BjMsn.Poliban', ip='10.3.0.3')
        h19 = self.addHost('Trk.U.Borneo', ip='10.3.0.4')
        h20 = self.addHost('Pangkep', ip='10.3.0.2')
        h21 = self.addHost('UNIMA Tomohon', ip='10.3.0.5')
        


        info( '*** Add links\n')
        self.addLink(s2, h1)
        self.addLink(s2, h2)
        self.addLink(s5, h3)
        self.addLink(s5, h4)
        self.addLink(s5, h5)
        self.addLink(s6, h8)
        self.addLink(s6, h7)
        self.addLink(s11, h9)
        self.addLink(s11, h22)
        self.addLink(s13, h10)
        self.addLink(s12, h6)
        self.addLink(s3, h6)
        self.addLink(s15, h12)
        self.addLink(s15, h11)
        self.addLink(s5, h6)
        self.addLink(s16, h13)
        self.addLink(s17, h14)
        self.addLink(s22, h18)
        self.addLink(s21, h19)
        self.addLink(s16, h15)
        self.addLink(s18, h16)
        self.addLink(s24, h20)
        self.addLink(s28, h21)
        self.addLink(s1, s2)
        self.addLink(s2, s5)
        self.addLink(s2, s3)
        self.addLink(s2, s11)
        self.addLink(s3, s4)
        self.addLink(s4, s6)
        self.addLink(s5, s7)
        self.addLink(s7, s8)
        self.addLink(s6, s8)
        self.addLink(s8, s11)
        self.addLink(s11, s9)
        self.addLink(s11, s10)
        self.addLink(s11, s12)
        self.addLink(s12, s20)
        self.addLink(s13, s15)
        self.addLink(s12, s14)
        self.addLink(s15, s17)
        self.addLink(s14, s16)
        self.addLink(s17, s16)
        self.addLink(s16, s21)
        self.addLink(s20, s23)
        self.addLink(s23, s22)
        self.addLink(s22, s21)
        self.addLink(s16, s24)
        self.addLink(s24, s25)
        self.addLink(s24, s26)
        self.addLink(s26, s27)
        self.addLink(s27, s28)
        self.addLink(s16, s18)
        self.addLink(s18, s19)

topos = { 'mytopo': ( lambda: MyTopo() ) }
    
if __name__ == '__main__':
    from onosnet import run
    run( MyTopo() )
