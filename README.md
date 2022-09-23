# organize-dowloads
It's just a simple script to automatically organize your download files

### If you want this to automatically run in the background follow this instructions

1) Press Windows key and R. This will open a small window.
2) Type **shell:startup** to open the startup folder
3) Now we'll create a small bash script with the following content
  
  @echo off
  
  "path to your python executable" "the location of your order.pyw"
  
  pause
  
  That's it!
  
  When you restart your PC the script shoud be working properly
