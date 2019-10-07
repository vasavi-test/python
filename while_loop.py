command = raw_input("enter command: ")
started=False
stopped=False
if command=="start":
    if started:
        print "already started."
    else:
        print "car started"
elif command=="stop":
    if stopped:
        print "already car stopped."
    else:
        print "car stopped"
elif command=="help":
    print """ start-----to start the car.
    stop------to stop the car.
    quit----to quit."""
else:
    quit()