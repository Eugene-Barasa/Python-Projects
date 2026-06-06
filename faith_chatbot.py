# ============================================
# FAITH & BIBLE ASSISTANT CHATBOT
# By Eugene Barasa — Maseno University
# "Work Faithfully. Grow Intentionally. Seek God Consistently."
# ============================================

import random
import datetime

# ============================================
# KNOWLEDGE BASE
# ============================================

# Bible Books
bible_books = {
    "old testament": ["Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy",
                      "Joshua", "Judges", "Ruth", "1 Samuel", "2 Samuel",
                      "1 Kings", "2 Kings", "1 Chronicles", "2 Chronicles",
                      "Ezra", "Nehemiah", "Esther", "Job", "Psalms", "Proverbs",
                      "Ecclesiastes", "Song of Solomon", "Isaiah", "Jeremiah",
                      "Lamentations", "Ezekiel", "Daniel", "Hosea", "Joel",
                      "Amos", "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk",
                      "Zephaniah", "Haggai", "Zechariah", "Malachi"],
    "new testament": ["Matthew", "Mark", "Luke", "John", "Acts", "Romans",
                      "1 Corinthians", "2 Corinthians", "Galatians", "Ephesians",
                      "Philippians", "Colossians", "1 Thessalonians", "2 Thessalonians",
                      "1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrews",
                      "James", "1 Peter", "2 Peter", "1 John", "2 John",
                      "3 John", "Jude", "Revelation"]
}

# Verses by topic
verses_by_topic = {
    "strength": [
        "I can do all things through Christ who strengthens me. — Philippians 4:13",
        "But those who hope in the Lord will renew their strength. — Isaiah 40:31",
        "The Lord is my strength and my shield. — Psalm 28:7",
        "Be strong and courageous. Do not be afraid. — Joshua 1:9"
    ],
    "love": [
        "For God so loved the world that he gave his one and only Son. — John 3:16",
        "Love is patient, love is kind. — 1 Corinthians 13:4",
        "We love because he first loved us. — 1 John 4:19",
        "Greater love has no one than this: to lay down one's life for one's friends. — John 15:13"
    ],
    "faith": [
        "Now faith is confidence in what we hope for. — Hebrews 11:1",
        "For we live by faith, not by sight. — 2 Corinthians 5:7",
        "If you have faith as small as a mustard seed, nothing will be impossible. — Matthew 17:20",
        "Trust in the Lord with all your heart. — Proverbs 3:5"
    ],
    "peace": [
        "Peace I leave with you; my peace I give you. — John 14:27",
        "And the peace of God, which transcends all understanding. — Philippians 4:7",
        "Be still and know that I am God. — Psalm 46:10",
        "Cast all your anxiety on him because he cares for you. — 1 Peter 5:7"
    ],
    "hope": [
        "For I know the plans I have for you, declares the Lord. — Jeremiah 29:11",
        "May the God of hope fill you with all joy and peace. — Romans 15:13",
        "And we know that in all things God works for the good. — Romans 8:28",
        "With God all things are possible. — Matthew 19:26"
    ],
    "wisdom": [
        "If any of you lacks wisdom, ask God, who gives generously. — James 1:5",
        "The fear of the Lord is the beginning of wisdom. — Proverbs 9:10",
        "Your word is a lamp for my feet, a light on my path. — Psalm 119:105",
        "All Scripture is God-breathed and useful for teaching. — 2 Timothy 3:16"
    ],
    "prayer": [
        "Ask and it will be given to you; seek and you will find. — Matthew 7:7",
        "Do not be anxious about anything, but in every situation, by prayer. — Philippians 4:6",
        "The prayer of a righteous person is powerful and effective. — James 5:16",
        "This is the confidence we have in approaching God. — 1 John 5:14"
    ],
    "forgiveness": [
        "If we confess our sins, he is faithful and just to forgive us. — 1 John 1:9",
        "For as far as the east is from the west, so far has he removed our transgressions. — Psalm 103:12",
        "Bear with each other and forgive one another. — Colossians 3:13",
        "Blessed is the one whose transgressions are forgiven. — Psalm 32:1"
    ]
}

# Christian concepts
concepts = {
    "salvation": "Salvation is the deliverance from sin and its consequences through faith in Jesus Christ. Romans 10:9 says: 'If you declare with your mouth Jesus is Lord and believe in your heart that God raised him from the dead, you will be saved.'",
    "grace": "Grace is God's unmerited favor toward humanity. Ephesians 2:8-9 says: 'For it is by grace you have been saved, through faith, and this is not from yourselves, it is the gift of God, not by works.'",
    "holy spirit": "The Holy Spirit is the third person of the Trinity. He guides, comforts, and empowers believers. John 14:26 says He is our Advocate who teaches us all things.",
    "trinity": "The Trinity refers to God existing as three persons: Father, Son (Jesus Christ), and Holy Spirit, while remaining one God. Matthew 28:19 mentions all three persons.",
    "baptism": "Baptism is an outward expression of an inward change. It symbolizes dying to the old self and rising to new life in Christ. Romans 6:4 describes this beautifully.",
    "communion": "Communion (The Lord's Supper) is a memorial of Jesus' sacrifice. The bread represents His body and the wine His blood. 1 Corinthians 11:24-25 gives the institution.",
    "repentance": "Repentance means turning away from sin and turning toward God. Acts 3:19 says: 'Repent and turn to God so that your sins may be wiped out.'",
    "discipleship": "Discipleship is following Jesus and helping others follow Him too. Matthew 28:19-20 gives the Great Commission to make disciples of all nations.",
    "worship": "Worship is giving honor and devotion to God. John 4:24 says true worshippers worship in Spirit and in truth.",
    "tithing": "Tithing means giving 10% of your income to God. Malachi 3:10 says: 'Bring the whole tithe into the storehouse... and see if I will not throw open the floodgates of heaven.'"
}

# Prayers
prayers = {
    "morning": "Heavenly Father, thank you for this new day. Guide my steps, guard my heart, and let Your light shine through me today. Give me wisdom for every decision and strength for every challenge. In Jesus name, Amen. 🙏",
    "evening": "Lord, thank you for bringing me safely through this day. Forgive me where I fell short. As I rest tonight, fill me with Your peace that surpasses all understanding. In Jesus name, Amen. 🙏",
    "strength": "Father, I need Your strength today. When I am weak, You are strong. Help me to rely on You and not my own understanding. Fill me with courage to face this day. In Jesus name, Amen. 🙏",
    "guidance": "Lord, I seek Your direction. Order my steps according to Your Word. Give me clarity, wisdom and discernment. Let Your will be done in my life. In Jesus name, Amen. 🙏",
    "thanksgiving": "God, I am grateful for Your love, grace and mercy. Thank You for life, health, family and every blessing. You are faithful and I praise Your holy name. In Jesus name, Amen. 🙏"
}

# Greetings
greetings = ["hello", "hi", "hey", "good morning", "good afternoon", "good evening", "greetings", "shalom"]

# Farewells
farewells = ["bye", "goodbye", "see you", "farewell", "exit", "quit", "stop", "end"]

# ============================================
# CHATBOT FUNCTIONS
# ============================================

def get_greeting():
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "Good morning"
    elif hour < 17:
        return "Good afternoon"
    else:
        return "Good evening"

def get_verse_by_topic(topic):
    for key in verses_by_topic:
        if key in topic:
            verses = verses_by_topic[key]
            return random.choice(verses)
    return None

def get_concept(message):
    for key in concepts:
        if key in message:
            return concepts[key]
    return None

def get_prayer(message):
    for key in prayers:
        if key in message:
            return prayers[key]
    return None

def list_bible_books(message):
    if "old testament" in message:
        books = bible_books["old testament"]
        return f"The Old Testament has {len(books)} books:\n" + ", ".join(books)
    elif "new testament" in message:
        books = bible_books["new testament"]
        return f"The New Testament has {len(books)} books:\n" + ", ".join(books)
    elif "books" in message or "bible" in message:
        ot = len(bible_books["old testament"])
        nt = len(bible_books["new testament"])
        return f"The Bible has {ot + nt} books total:\n- Old Testament: {ot} books\n- New Testament: {nt} books\nAsk me about 'Old Testament books' or 'New Testament books' for the full list!"
    return None

def get_devotional():
    devotionals = [
        "Today's Devotional 📖\n\nGod has a plan for your life that is greater than anything you can imagine. Even when the path seems unclear, trust that He is ordering your steps. Keep walking in faith!\n\nVerse: Jeremiah 29:11",
        "Today's Devotional 📖\n\nYour faithfulness today is building a testimony for tomorrow. Don't despise small beginnings. Every step of obedience matters to God.\n\nVerse: Zechariah 4:10",
        "Today's Devotional 📖\n\nGod's grace is sufficient for every challenge you face today. You don't have to be perfect — just willing. He does His best work through yielded hearts.\n\nVerse: 2 Corinthians 12:9",
        "Today's Devotional 📖\n\nPrayer is your direct line to Heaven. Don't let the busyness of life crowd out your time with God. In His presence is where you find strength for the journey.\n\nVerse: Philippians 4:6-7",
    ]
    return random.choice(devotionals)

def save_conversation(history):
    filename = f"conversation_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        f.write("FAITH & BIBLE ASSISTANT — Conversation Log\n")
        f.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 50 + "\n\n")
        for entry in history:
            f.write(entry + "\n")
    return filename

def get_response(message, history):
    message = message.lower().strip()

    # Greetings
    if any(g in message for g in greetings):
        return f"{get_greeting()}! I am your Faith & Bible Assistant. 🙏\nHow can I help you today? You can ask me about:\n- Bible verses (e.g. 'verse about strength')\n- Christian concepts (e.g. 'what is grace')\n- Prayers (e.g. 'morning prayer')\n- Bible books (e.g. 'books of the Bible')\n- Devotional (type 'devotional')"

    # Farewells
    if any(f in message for f in farewells):
        filename = save_conversation(history)
        return f"God bless you! 🙏\nRemember: Work Faithfully. Grow Intentionally. Seek God Consistently.\nConversation saved to {filename}"

    # Devotional
    if "devotional" in message:
        return get_devotional()

    # Bible books
    books_response = list_bible_books(message)
    if books_response:
        return books_response

    # Verses by topic
    verse = get_verse_by_topic(message)
    if verse:
        return f"Here's a verse for you 📖\n\n{verse}"

    # Christian concepts
    concept = get_concept(message)
    if concept:
        return f"📖 {concept}"

    # Prayers
    prayer = get_prayer(message)
    if prayer:
        return f"Here's a prayer for you 🙏\n\n{prayer}"

    # Help
    if "help" in message:
        return "I can help you with:\n1. Bible verses — 'verse about faith/love/peace/strength/hope/wisdom/prayer/forgiveness'\n2. Christian concepts — 'what is salvation/grace/trinity/baptism/repentance'\n3. Prayers — 'morning/evening/strength/guidance/thanksgiving prayer'\n4. Bible books — 'books of the Bible/Old Testament/New Testament'\n5. Devotional — type 'devotional'\n6. Save & exit — type 'bye'"

    # Default
    responses = [
        "That's a great question! I'm still learning. Try asking about a Bible verse, prayer, or Christian concept. 🙏",
        "I may not have that answer yet, but God does! Try asking about 'verse about hope' or 'what is grace'. 😊",
        "Interesting! For now I can help with Bible verses, prayers and Christian concepts. Type 'help' to see all options. 🙏",
    ]
    return random.choice(responses)

# ============================================
# MAIN PROGRAM
# ============================================

def main():
    history = []

    print("\n" + "=" * 55)
    print("    ✝  FAITH & BIBLE ASSISTANT  ✝")
    print("    By Eugene Barasa — Maseno University")
    print("=" * 55)
    print(f"\n{get_greeting()}! Welcome to your Faith & Bible Assistant 🙏")
    print("Type 'help' to see what I can do.")
    print("Type 'bye' to exit and save conversation.")
    print("-" * 55)

    while True:
        user_input = input("\nYou: ").strip()

        if not user_input:
            continue

        history.append(f"You: {user_input}")
        response = get_response(user_input, history)
        history.append(f"Bot: {response}")

        print(f"\n Eagle Assistant 🦅: {response}")
        print("-" * 55)

        if any(f in user_input.lower() for f in farewells):
            break

main()
