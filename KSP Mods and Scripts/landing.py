<<<<<<< HEAD
import krpc
import time
conn = krpc.connect()

def main():
    print('Connecting to server')
    vessel = conn.space_center.active_vessel
    obt_frame = vessel.orbit.body.non_rotating_reference_frame
    srf_frame = vessel.orbit.body.reference_frame
    altitude = conn.add_stream(getattr, vessel.flight(), 'surface_altitude')
    #speed tracking  
    def speedReadout():
        obt_speed = vessel.flight(obt_frame).speed
        srf_speed = vessel.flight(srf_frame).speed
        vrt_speed = vessel.flight(srf_frame).vertical_speed
        print('Orbital speed = %.1f m/s, Surface speed = %.1f m/s, Vertical speed = %.1f' %
            (obt_speed, srf_speed, vrt_speed,))
    #retrograde
    ap = vessel.auto_pilot
    ap.sas = True
    ap.sas_mode = ap.sas_mode.retrograde   
    print('Vessel retrograde\n', speedReadout())    
    #landing
    stage = 2
    while True:
        if altitude() in range(2000,100) & stage == 2:    
            vessel.control.toggle_action_group(9)
            print('Parachutes Armed')
            stage = stage - 1
        if altitude() in range(2,-2) & stage == 1:
            vessel.control.toggle_action_group(10)
            print('Antenna Deployed')
            stage = stage - 1
=======
import krpc
import time
conn = krpc.connect()

def main():
    print('Connecting to server')
    vessel = conn.space_center.active_vessel
    obt_frame = vessel.orbit.body.non_rotating_reference_frame
    srf_frame = vessel.orbit.body.reference_frame
    altitude = conn.add_stream(getattr, vessel.flight(), 'surface_altitude')
    #speed tracking  
    def speedReadout():
        obt_speed = vessel.flight(obt_frame).speed
        srf_speed = vessel.flight(srf_frame).speed
        vrt_speed = vessel.flight(srf_frame).vertical_speed
        print('Orbital speed = %.1f m/s, Surface speed = %.1f m/s, Vertical speed = %.1f' %
            (obt_speed, srf_speed, vrt_speed,))
    #retrograde
    ap = vessel.auto_pilot
    ap.sas = True
    ap.sas_mode = ap.sas_mode.retrograde   
    print('Vessel retrograde\n', speedReadout())    
    #landing
    stage = 2
    while True:
        if altitude() in range(2000,100) & stage == 2:    
            vessel.control.toggle_action_group(9)
            print('Parachutes Armed')
            stage = stage - 1
        if altitude() in range(2,-2) & stage == 1:
            vessel.control.toggle_action_group(10)
            print('Antenna Deployed')
            stage = stage - 1
>>>>>>> 9eba8363b33dca44ef9a57a641c922f888204e9b
main()      