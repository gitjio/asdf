set ns [new Simulator]

#Open the nam trace file
set nf [open out.nam w]
$ns namtrace-all Snf
#Define a 'finish' procedure
proc finish {} {
     global ns nf
$ns flush-trace
#Close the trace file
close $nf
#Executenam on the trace file
exec nam out.nam &
exit0
}

#Create four nodes
set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]


#Change the shape of center node in a star topology
$nO shape square

#Create links between the nodes
$ns duplex- link $n0 $n1 1Mb 10ms DropTail
$ns duplex- link $n0 $n2 1Mb 10ms DropTail
$ns duplex-link $n0 $n3 1Mb 10ms DropTail
$ns duplex-link $n0 $n4 1Mb 10ms DropTail
$ns duplex- link $n0 $n5 1Mb 10ms DropTail


set tcp0 [new Agent/TCP]
$tcp0 set class_1

$ns attach-agent $n1 $tcp0
#Create a TCP sink agent (a traffic sink) for TCP and attach it to node n3
set sink0 [new Agent/TCPSink]
$ns attach-agent $n3 $sink0
#Connect the traffic sources with the traffic sink
Sns connect Stcp0 $sinko
 # Create a CBR traffic source and attach it to tpo
set cbr0 [new Application/Traffic/CBR]
Scbro set packetsize_500
Scbr0 set interval_0.01
$cbrO attach-agent $tcp0

#Schedule events for the CB agents
$ns at 0.5 "$cbr0 start'
$ns at 4.5 "$ebr0 stop"


#Call the finish procedure after 5 seconds of simulation time
$ns at 5.0 "finish
#Run the simulation
$ns run
