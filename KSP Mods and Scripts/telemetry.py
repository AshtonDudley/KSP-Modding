import krpc
import time
import os.path
conn = krpc.connect()

def main():
    print('Connecting to server')
    
    vessel = conn.space_center.active_vessel
    obt_frame = vessel.orbit.body.non_rotating_reference_frame
    srf_frame = vessel.orbit.body.reference_frame
    track = True
    log = False

    file = open('C:/Users/Ashton/Desktop/Code, Modding & Backups/KSP Mods and Scripts/speedlog.txt','w+')        

    while track == True:
        try:
            obt_speed = vessel.flight(obt_frame).speed
            srf_speed = vessel.flight(srf_frame).speed
            vrt_speed = vessel.flight(srf_frame).vertical_speed

            print('Orbital speed = %.1f m/s, Surface speed = %.1f m/s, Vertical speed = %.1f' % (obt_speed, srf_speed, vrt_speed,))
            
            file.write('Orbital speed = %.1f m/s, Surface speed = %.1f m/s, Vertical speed = %.1f\r' % (obt_speed, srf_speed, vrt_speed,))
            
            time.sleep(1)
        except KeyboardInterrupt:
            file.close()
            track = False
            pass
    while log == True:
        for i in range(10):
            return  
    print('finished')
main()