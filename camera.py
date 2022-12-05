if camlist:
    
    # Initialize and start camera  
    cam = pygame.camera.Camera(camlist[0], (640, 480))
    cam.start()
    
    # capturing the single image
    image = cam.get_image()
    
    # saving the image
    pygame.image.save(image, "filename.jpg")
    
else:
   if camera is not detected the moving to this part