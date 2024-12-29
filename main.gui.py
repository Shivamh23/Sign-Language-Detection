# GUI
root = tk.Tk()
root.title('Sign Language Detection')

Label(root, text='Sign Language Detection', font=('Arial', 16)).pack(pady=10)

upload_button = Button(root, text='Upload Image', command=upload_image)
upload_button.pack(pady=5)

video_button = Button(root, text='Start Real-Time Detection', command=start_video)
video_button.pack(pady=5)

result_label = Label(root, text='', font=('Arial', 12))
result_label.pack(pady=10)

root.mainloop()
