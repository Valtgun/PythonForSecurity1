from mpi4py import MPI
import hashlib
import itertools
import string
import time

def md5_crack(target_hash, charset, max_length, rank, size):
    for length in range(1, max_length + 1):
        # Divide workload
        combinations = itertools.islice(
            itertools.product(charset, repeat=length),
            rank, None, size
        )

        for candidate in combinations:
            password = ''.join(candidate)
            hashed_password = hashlib.md5(password.encode()).hexdigest()

            if hashed_password == target_hash:
                return password  # Found the password
    return None  # Not found

if __name__ == "__main__":
    # MPI setup
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    target_hash = "296ab79bb0e6b305a21f964bd2ac8531"  # MD5 hash of "hellow"
    charset = string.ascii_lowercase  # Use lowercase letters
    max_length = 6  # Maximum password length to try

    # Start timer
    if rank == 0:
        start_time = time.time()

    # Crack
    result = md5_crack(target_hash, charset, max_length, rank, size)

    # Gather results
    found_password = comm.gather(result, root=0)

    # Display results
    if rank == 0:
        # Stop timer
        end_time = time.time()

        found_password = next((pwd for pwd in found_password if pwd), None)
        if found_password:
            print(f"Password found: {found_password}")
        else:
            print("Password not found.")

        print(f"Laiks: {end_time - start_time:.2f} sek, {size} procesi.")