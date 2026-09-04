import random
import time

print("[1 = NumberGuessingGame | 2 = RandomSentences]")
promptAnswer = int(input("enter your choice (1 or 2): "))
PfileLines = [
    '/system/core/kernel_modules/',
    '/usr/local/lib/critical_drivers/',
    '/home/user/Documents/tax_records_2024/',
    '/home/user/Pictures/family_vacation_backup/,
    '/var/log/system_events/',
    '/etc/network/security_certs/',
    '/home/user/Desktop/thesis_final_draft/',
    '/opt/steam/steamapps/common/',
    '/home/user/Downloads/important_project/',
    '/System/Library/PreferenceFiles/',
    '/boot/grub/config_backup/',
    '/home/user/.ssh/keys/',
    '/var/www/html/production_site/',
    '/home/user/Music/rare_collection/',
    '/usr/share/fonts/custom_fonts/',
    '/home/user/Videos/wedding_footage/',
    '/etc/cron.d/scheduled_tasks/',
    '/home/user/AppData/save_files/',
    '/media/external_drive/backup_2024/',
    '/home/user/.config/game_saves/',
]
PdeleteLines = [
    'system32_backup.dll',
    'user_credentials.db',
    'master_password_vault.enc',
    'encryption_keys.pem',
    'financial_records_2024.xlsx',
    'tax_return_final.pdf',
    'company_database_dump.sql',
    'private_messages_archive.zip',
    'security_cert_root.crt',
    'network_config_master.cfg',
    'game_save_slot_01.dat',
    'game_save_slot_02.dat',
    'photo_album_master.zip',
    'family_photos_2024.zip',
    'wedding_video_final_edit.mp4',
    'thesis_chapter_final.docx',
    'project_source_code.zip',
    'ssh_private_key.pem',
    'browser_history_export.db',
    'contact_list_backup.vcf',
    'email_archive_2024.pst',
    'license_keys_master.txt',
    'admin_panel_credentials.txt',
    'server_root_access.log',
    'firmware_update_critical.bin',
    'boot_sector_backup.img',
    'registry_hive_backup.reg',
    'vpn_config_secure.ovpn',
    'crypto_wallet_seed.txt',
    'api_keys_production.env',    
]

count1 = 0
count2 = 0

if promptAnswer == 1:
    for i in range(3):
        count1 = count1 + 1
        if count1 == 1:
            print("[#..]")
            time.sleep(1)
        elif count1 == 2:
            print("[##.]")
            time.sleep(1)
        elif count1 == 3:
            print("[###]")
            time.sleep(1)
    time.sleep(1)
    print("-- number guessing game --")
    print("[NOTE: if you guess the wrong number, your files and directories will be deleted]")
    time.sleep(0.5)
    print("guess a random number from 1-10")
    rightNumber = random.randint(1, 10)
    guess = int(input("enter your guess: "))
    if guess == rightNumber:
        print("you guessed the right number!")
    elif promptAnswer > 10 or promptAnswer < 1:
        print("invalid choice, please try again.")
    else:
        print("wrong number, the right number was " + str(rightNumber))
        time.sleep(0.7)
        print("[WARNING: your files and directories will be deleted!]")
        print("deleting files and directories in...")
        time.sleep(0.6)
        print("3...")
        time.sleep(0.6)
        print("2..")
        time.sleep(0.6)
        print("1.")
        time.sleep(0.6)
        for i in range(30)

        
elif promptAnswer == 2:
    for i in range(3):
        count2 = count2 + 1
        if count2 == 1:
            print("[#..]")
            time.sleep(1)
        elif count2 == 2:
            print("[##.]")
            time.sleep(1)
        elif count2 == 3:
            print("[###]")
            time.sleep(1)
    print("-- random sentence generator --")
    time.sleep(0.5)
    
else:
    print("invalid choice, please try again.")
