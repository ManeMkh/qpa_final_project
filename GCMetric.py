import matplotlib.pyplot as plt
final_output = []

# calculating GC-content ratio using the formula
def ratio(seq):
    count_a = seq.count("A")
    count_g = seq.count("G")
    count_c = seq.count("C")
    count_t = seq.count("T")
    total = count_a + count_g + count_c + count_t
    if total != 0:
        return (count_c+count_g)/total * 100

# plotting the ratio

def project(seq):
    for i in range(len(seq)):
        s = seq[i:i+100]
        gc = ratio(s)
        final_output.append(gc)
    plt.plot(final_output)
    plt.xlabel("Genome position")
    plt.ylabel("GC-content(%)")
    plt.savefig("output.jpg")
    plt.show()


with open(r'covid.txt') as file:
    data = file.read()

project(data)
