from keyword_extraction import get_link_sugessions

doc1 = '''
    A blockchain is a growing list of records, called blocks, that are linked together using cryptography. Each block contains a cryptographic hash of the previous block, 
    a timestamp, and transaction data (generally represented as a Merkle tree). The timestamp proves that the transaction data existed when the block was published to get 
    into its hash. As blocks each contain information about the block previous to it, they form a chain, with each additional block reinforcing the ones before it. Therefore, 
    blockchains are resistant to modification of their data because once recorded, the data in any given block cannot be altered retroactively without altering all subsequent blocks.
    Blockchains are typically managed by a peer-to-peer network for use as a publicly distributed ledger, where nodes collectively adhere to a protocol to communicate and 
    validate new blocks. Although blockchain records are not unalterable as forks are possible, blockchains may be considered secure by design and exemplify a distributed 
    computing system with high Byzantine fault tolerance. The blockchain was popularized by a person (or group of people) using the name Satoshi Nakamoto in 2008 to serve 
    as the public transaction ledger of the cryptocurrency bitcoin, based on work by Stuart Haber, W. Scott Stornetta, and Dave Bayer. The identity of Satoshi Nakamoto 
    remains unknown to date. The implementation of the blockchain within bitcoin made it the first digital currency to solve the double-spending problem without the need 
    of a trusted authority or central server. The bitcoin design has inspired other applications and blockchains that are readable by the public and are widely used by 
    cryptocurrencies. The blockchain is considered a type of payment rail. Private blockchains have been proposed for business use. Computerworld called the marketing of 
    such privatized blockchains without a proper security model "snake oil"; however, others have argued that permissioned blockchains, if carefully designed, may be more 
    decentralized and therefore more secure in practice than permissionless ones.
'''

doc2 = '''
    Machine learning (ML) is the study of computer algorithms that can improve automatically through experience and by the use of data. It is seen as a part of artificial intelligence. 
    Machine learning algorithms build a model based on sample data, known as training data, in order to make predictions or decisions without being explicitly programmed to do so. 
    Machine learning algorithms are used in a wide variety of applications, such as in medicine, email filtering, speech recognition, and computer vision, where it is difficult or 
    unfeasible to develop conventional algorithms to perform the needed tasks. A subset of machine learning is closely related to computational statistics, which focuses on making 
    predictions using computers; but not all machine learning is statistical learning. The study of mathematical optimization delivers methods, theory and application domains to the 
    field of machine learning. Data mining is a related field of study, focusing on exploratory data analysis through unsupervised learning. Some implementations of machine learning 
    use data and neural networks in a way that mimics the working of a biological brain. In its application across business problems, machine learning is also referred to as predictive 
    analytics. 
'''

links = get_link_sugessions(doc1, num_keywords=5, num_links=5)
print(links)

links2 = get_link_sugessions(doc2)
print(links2)
