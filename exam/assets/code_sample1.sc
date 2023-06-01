import shared3p;
import shared3p_random;
import stdlib;

domain pd_shared3p shared3p;

// This function generates a random array of specified length and maximum value.
template<domain D : shared3p>
D uint64[[1]] generate_random_array(uint length, uint max_value) {
    D uint64[[1]] a (length);
    a = randomize (a); // Randomize the values in the array.
    a = a % max_value; // Limit the values to be within the range [0, max_value).
    return a;
}

// This function counts the occurrences of a specified value (needle) in an input array (haystack).
template<domain D : shared3p>
D uint64 count_if(D uint64[[1]] haystack, D uint64 needle) {
        D bool[[1]] b = haystack == needle; // Create a boolean array marking where the needle is found.
        return sum(b); // Sum the boolean array to count the occurrences of the needle.
}

void main() {
    uint testsize = 100;
    uint64 maxvalue = 10;
    print("Generating random array of size ", testsize, " with values 0 to ", maxvalue);
    pd_shared3p uint64[[1]] testarray = generate_random_array (testsize, maxvalue);

    for (uint64 i = 0; i < maxvalue; i++) {
        pd_shared3p uint needle = i;
        pd_shared3p uint64 count = count_if (testarray, needle);
        print ("Value ", i, " occurs in array ", declassify(count), " times.");
    }
    /*
    Input leakage and privacy analysis:
    In this code, the only input that is declassified is the count of occurrences of each value in the array.
    There is no direct leakage of the input array itself or its contents.
    However, depending on the size of the input array and the maximum value, an adversary might be able to infer
    some information about the input array by observing the counts of occurrences.
    In this specific example, the risk to privacy is low, as the input array is randomly generated.
    /*

    /*
    04:31:24 Starting external tool "/usr/local/sharemind/bin/sm_compile_and_run.sh /home/sharemind/Downloads/secrec-task1_done.sc.txt"
    Using SHAREMIND_INSTALL_PREFIX='/usr/local/sharemind'
    Compiling: '/home/sharemind/Downloads/secrec-task1_done.sc.txt' to '/home/sharemind/Downloads/secrec-task1_done.sc.txtsb'
    Running: '/home/sharemind/Downloads/secrec-task1_done.sc.txtsb'
    2023.04.30 04:31:24 INFO    [Emulator][TdbModule] Loaded database module "tabledb_hdf5" (16 syscalls) from "libsharemind_mod_tabledb_hdf5.so" using API version 1.
    Generating random array of size 100 with values 0 to 10
    Value 0 occurs in array 8 times.
    Value 1 occurs in array 10 times.
    Value 2 occurs in array 11 times.
    Value 3 occurs in array 15 times.
    Value 4 occurs in array 12 times.
    Value 5 occurs in array 7 times.
    Value 6 occurs in array 10 times.
    Value 7 occurs in array 10 times.
    Value 8 occurs in array 5 times.
    Value 9 occurs in array 12 times.
    Process returned status: 0
    Estimated running time: 48199 microseconds (0 seconds)
    (This is the estimated running time of the program on the Sharemind Application Server, running on a 1 Gbit network)
    04:31:24 "/usr/local/sharemind/bin/sm_compile_and_run.sh" finished
    /*
}
