# You will be given a simplistic version of an FSM to code for a basic TCP session.
# The outcome of this exercise will be to return the correct state of the TCP FSM 
# based on the array of events given.

# The input array of events will consist of one or more of the following strings:
# APP_PASSIVE_OPEN, APP_ACTIVE_OPEN, APP_SEND, APP_CLOSE, APP_TIMEOUT, RCV_SYN, 
# RCV_ACK, RCV_SYN_ACK, RCV_FIN, RCV_FIN_ACK

# The states are as follows and should be returned in all capital letters as shown:
# CLOSED, LISTEN, SYN_SENT, SYN_RCVD, ESTABLISHED, CLOSE_WAIT, LAST_ACK, FIN_WAIT_1, 
# FIN_WAIT_2, CLOSING, TIME_WAIT

# Your job is to traverse the FSM as determined by the events, 
# and return the proper state as a string, all caps, as shown above.

# If an event is not applicable to the current state, your code will return "ERROR".

# Action of each event upon each state are given.
# (the format is INITIAL_STATE: EVENT -> NEW_STATE)


def traverse_TCP_states(events):
    
    state = "CLOSED"  # initial state, always
    ACTIONS = {("CLOSED","APP_PASSIVE_OPEN") : "LISTEN",
             ("CLOSED","APP_ACTIVE_OPEN") : "SYN_SENT",
             ("LISTEN","RCV_SYN") : "SYN_RCVD",
             ("LISTEN","APP_SEND") : "SYN_SENT",
             ("LISTEN","APP_CLOSE") : "CLOSED",
             ("SYN_RCVD","APP_CLOSE") : "FIN_WAIT_1",
             ("SYN_RCVD","RCV_ACK") : "ESTABLISHED",
             ("SYN_SENT","RCV_SYN") : "SYN_RCVD",
             ("SYN_SENT","RCV_SYN_ACK") : "ESTABLISHED",
             ("SYN_SENT","APP_CLOSE") : "CLOSED",
             ("ESTABLISHED","APP_CLOSE") : "FIN_WAIT_1",
             ("ESTABLISHED","RCV_FIN") : "CLOSE_WAIT",
             ("FIN_WAIT_1","RCV_FIN") : "CLOSING",
             ("FIN_WAIT_1","RCV_FIN_ACK") : "TIME_WAIT",
             ("FIN_WAIT_1","RCV_ACK") : "FIN_WAIT_2",
             ("CLOSING","RCV_ACK") : "TIME_WAIT",
             ("FIN_WAIT_2","RCV_FIN") : "TIME_WAIT",
             ("TIME_WAIT","APP_TIMEOUT") : "CLOSED",
             ("CLOSE_WAIT","APP_CLOSE") : "LAST_ACK",
             ("LAST_ACK","RCV_ACK") : "CLOSED"}
    
    for event in events:
        if (state,event) in ACTIONS:
            state = ACTIONS[state,event]
        else:
            return "ERROR"
    return state

         
