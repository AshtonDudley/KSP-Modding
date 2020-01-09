<<<<<<< HEAD
import krpc
import time
conn = krpc.connect()

def main():
    print('Connecting to server')
    vessel = conn.space_center.active_vessel
    obt_frame = vessel.orbit.body.non_rotating_reference_frame
    srf_frame = vessel.orbit.body.reference_frame
    spd_track = True
    tgt_angle = 0
    while spd_track == True:
        obt_speed = vessel.flight(obt_frame).speed
        srf_speed = vessel.flight(srf_frame).speed
        vrt_speed = vessel.flight(srf_frame).vertical_speed
        print('Orbital speed = %.1f m/s, Surface speed = %.1f m/s, Vertical speed = %.1f' %
            (obt_speed, srf_speed, vrt_speed,))
        if vrt_speed in range(tgt_angle - 1,tgt_angle + 1):
            if vrt_speed in range(-0.1,0.1):  
                print('good')
            elif vrt_speed <- tgt_angle - 1 :
                print('too low')
                vessel.control.pitch = 0.05                
            elif vrt_speed <- tgt_angle + 1:
                print('too high')   
                vessel.control.pitch = 0.05            
        elif vrt_speed <= tgt_angle - 1:
            print('very low')
            vessel.control.pitch = 0.2
        elif vrt_speed >= tgt_angle + 1:
            print('very high')
            vessel.control.pitch = -0.2

    
    time.sleep(1)
=======
import krpc
import time
conn = krpc.connect()

def main():
    print('Connecting to server')
    vessel = conn.space_center.active_vessel
    obt_frame = vessel.orbit.body.non_rotating_reference_frame
    srf_frame = vessel.orbit.body.reference_frame
    spd_track = True
    tgt_angle = 0
    while spd_track == True:
        obt_speed = vessel.flight(obt_frame).speed
        srf_speed = vessel.flight(srf_frame).speed
        vrt_speed = vessel.flight(srf_frame).vertical_speed
        print('Orbital speed = %.1f m/s, Surface speed = %.1f m/s, Vertical speed = %.1f' %
            (obt_speed, srf_speed, vrt_speed,))
        if vrt_speed in range(tgt_angle - 1,tgt_angle + 1):
            if vrt_speed in range(-0.1,0.1):  
                print('good')
            elif vrt_speed <- tgt_angle - 1 :
                print('too low')
                vessel.control.pitch = 0.05                
            elif vrt_speed <- tgt_angle + 1:
                print('too high')   
                vessel.control.pitch = 0.05            
        elif vrt_speed <= tgt_angle - 1:
            print('very low')
            vessel.control.pitch = 0.2
        elif vrt_speed >= tgt_angle + 1:
            print('very high')
            vessel.control.pitch = -0.2

    
    time.sleep(1)
>>>>>>> 9eba8363b33dca44ef9a57a641c922f888204e9b
main()  