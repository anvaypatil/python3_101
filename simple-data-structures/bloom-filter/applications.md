### Applications of bloom filter
- Weak password detection
- Internet Cache Protocol
- Safe browsing in Google Chrome
- Wallet synchronization in Bitcoin
- Hash based IP Traceback
- Cyber security like virus scanning

### Extensions and applications
- Cache filtering
- Avoiding false positives in a finite universe
- Counting Bloom filters
- Decentralized aggregation
- Distributed Bloom filters
- Data synchronization
- Bloomier filters
- Compact approximators
- Parallel Partitioned Bloom Filters
- Stable Bloom filters
- Scalable Bloom filters
- Spatial Bloom filters
- Layered Bloom filters
- Attenuated Bloom filters
- Chemical structure searching

- You’ve seen in our given example that we could’ve use it to warn the user for weak passwords.
- You can use bloom filter to prevent your users from accessing malicious sites.
- Instead of making a query to an SQL database to check if a user with a certain email exists, you could first use a bloom filter for an inexpensive lookup check. If the email doesn’t exist, great! If it does exist, you might have to make an extra query to the database. You can do the same to search for if a ‘Username is already taken’.
- You can keep a bloom filter based on the IP address of the visitors to your website to check if a user to your website is a ‘returning user’ or a ‘new user’. Some false positive value for ‘returning user’ won’t hurt you, right?
- You can also make a Spell-checker by using bloom filter to track the dictionary words.
- Want to know how Medium used bloom filter to decide if a user already read post? Read this mind-blowing, freaking awesome article about it.