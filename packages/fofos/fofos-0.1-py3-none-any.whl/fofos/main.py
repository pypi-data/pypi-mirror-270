Bankers = """
#include <iostream>
#include <cstring> 
using namespace std;

const int MAX = 10;

void ShowFinalAvailable(int available[], int m) {
    cout << "final available resource:";
    for (int i = 0; i < m; i++) {
        cout << available[i] << ":";
    }
    cout << endl;
}

void calNeed(int need[], int maxi[][MAX], int alloc[][MAX], int n, int m) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            need[i * m + j] = maxi[i][j] - alloc[i][j];
        }
    }
}

bool isSafe(int process[], int avail[], int maxi[][MAX], int alloc[][MAX], int n, int m) {
    int need[MAX * MAX];
    calNeed(need, maxi, alloc, n, m);
    bool finish[MAX] = {false};
    int work[MAX];
    for (int i = 0; i < m; i++) {
        work[i] = avail[i];
    }
    int c = 0;
    while (c < n) {
        bool found = false;
        for (int i = 0; i < n; i++) {
            if (!finish[i]) {
                int j;
                for (j = 0; j < m; j++) {
                    if (need[i * m + j] > work[j]) {
                        break;
                    }
                }
                if (j == m) {
                    for (int k = 0; k < m; k++) {
                        work[k] += alloc[i][k];
                    }
                    process[c++] = i;
                    finish[i] = true;
                    found = true;
                }
            }
        }
        if (!found) {
            return false;
        }
    }
    return true;
}

int main() {
    int process[MAX], available[MAX], maxi[MAX][MAX], alloc[MAX][MAX];
    int n, m;
    cout << "Enter the number of processes:";
    cin >> n;
    cout << "Enter the number of resources:";
    cin >> m;
    cout << "Enter the available resources:"<<endl;
    for (int i = 0; i < m; i++) {
        cin >> available[i];
    }
    cout << "Enter the maximum resources for each process: "<<endl;
    for (int i = 0; i < n; i++) {
        cout << "Process " << i << ":";
        for (int j = 0; j < m; j++) {
            cin >> maxi[i][j];
        }
    }
    cout << "Enter the allocated resources for each process: "<<endl;
    for (int i = 0; i < n; i++) {
        cout << "Process " << i << ":";
        for (int j = 0; j < m; j++) {
            cin >> alloc[i][j];
        }
    }
    if (isSafe(process, available, maxi, alloc, n, m)) {
        cout << "The system is in a safe state."<<endl<<"Safe sequence: <";
        for (int i = 0; i < n; i++) {
            cout << "P" << process[i];
            if (i != n - 1) {
                cout << ",";
            }
        }
        cout << ">"<<endl;
        ShowFinalAvailable(available, m);
    } else {
        cout << "The system is not in a safe state."<<endl;
    }
    return 0;
}

// ***************** Output ****************

// Enter the number of processes:5  
// Enter the number of resources:3
// Enter the available resources: 3 3 2
// Enter the maximum resources for each process: 
// Process 0:7 5 3
// Process 1:3 2 2
// Process 2:9 0 2
// Process 3:2 2 2
// Process 4:4 3 3
// Enter the allocated resources for each process: 
// Process 0:0 1 0
// Process 1:2 0 0
// Process 2:3 0 2
// Process 3:2 1 1
// Process 4:0 0 2
// The system is in a safe state.
// Safe sequence: <P1,P3,P4,P0,P2>
// final available resource:3:3:2:
"""

FCFS_AND_SSTF = """
#include <iostream>
#include <cmath>
#include <algorithm>
#include <climits>
using namespace std;

void FCFS(int arr[], int size, int head);
void SSTF(int arr[], int size, int head);

int main()
{
    int choice;
    int size;
    int arr[100];
    int size_sstf;
    int arr_sstf[100];

    while (true) {
        cout << "Choose a scheduling algorithm:" << endl;
        cout << "1. First-Come-First-Serve (FCFS)" << endl;
        cout << "2. Shortest Seek Time First (SSTF)" << endl;
        cout << "3. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;
        switch (choice) {
            case 1:
                cout << "Enter the number of requests: ";
                cin >> size;
                cout << "Enter the requests:" << endl;
                for (int i = 0; i < size; ++i) {
                    cin >> arr[i];
                }
                int head;
                cout << "Enter the initial head position: ";
                cin >> head;
                FCFS(arr, size, head);
                break;
            case 2:
                cout << "Enter the number of requests: ";
                cin >> size_sstf;
                cout << "Enter the requests:" << endl;
                for (int i = 0; i < size_sstf; ++i) {
                    cin >> arr_sstf[i];
                }
                int head_sstf;
                cout << "Enter the initial head position: ";
                cin >> head_sstf;
                SSTF(arr_sstf, size_sstf, head_sstf);
                break;
            case 3:
                exit(0);
            default:
                cout << "Invalid choice! Exiting." << endl;
                break;
        }
    }
    return 0;
}


void FCFS(int arr[], int size, int head)
{
    int seek_count = 0;
    int distance, cur_track;

    for (int i = 0; i < size; i++) {
        cur_track = arr[i];
        distance = abs(cur_track - head);
        seek_count += distance;
        head = cur_track;
    }

    cout << "Total number of seek operations = " << seek_count << endl;
    cout << "Seek Sequence is" << endl<<endl;
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " -> ";
    }
    cout<<"END"<<endl<<endl;
}

void SSTF(int arr[], int size, int head)
{
    int seek_count = 0;
    int cur_track = head;

    bool visited[size] = {false};

    cout << "Seek Sequence is : "<<endl<<endl ;
    for (int i = 0; i < size; i++) {
        int min_distance = INT_MAX;
        int min_index = -1;
        for (int j = 0; j < size; j++) {
            if (!visited[j]) {
                int temp_distance = abs(arr[j] - cur_track);
                if (temp_distance < min_distance) {
                    min_distance = temp_distance;
                    min_index = j;
                }
            }
        }
        seek_count += min_distance;
        cur_track = arr[min_index];
        visited[min_index] = true;
        cout << cur_track << " -> ";
    }

    cout<<"END"<<endl<<endl;
    cout << "Total number of seek operations = " << seek_count << endl<<endl;
}

// ***************** Output ******************

// Choose a scheduling algorithm:
// 1. First-Come-First-Serve (FCFS)
// 2. Shortest Seek Time First (SSTF)
// 3. Exit
// Enter your choice: 1
// Enter the number of requests: 11
// Enter the requests:
// 45 21 67 90 4 50 89 52 61 87 25
// Enter the initial head position: 50
// Total number of seek operations = 403
// Seek Sequence is

// 45 -> 21 -> 67 -> 90 -> 4 -> 50 -> 89 -> 52 -> 61 -> 87 -> 25 -> END

// Choose a scheduling algorithm:
// 1. First-Come-First-Serve (FCFS)
// 2. Shortest Seek Time First (SSTF)
// 3. Exit
// Enter your choice: 2
// Enter the number of requests: 10
// Enter the requests:
// 45 21 67 90 4 89 52 61 87 25    
// Enter the initial head position: 50
// Seek Sequence is : 

// 52 -> 45 -> 61 -> 67 -> 87 -> 89 -> 90 -> 25 -> 21 -> 4 -> END

// Total number of seek operations = 140

"""

FCFS = """
#include<iostream>
using namespace std;
int main()
{   int n,bt[20],wt[20],tat[20],avwt=0,i,j;
    float avtat=0;
    cout<<"Enter number of processes : ";
    cin>>n;

    cout<<"\\nEnter Burst Time\\n";
    for(i=0;i<n;i++)
    {
        cout<<"P["<<i+1<<"]: ";
        cin>>bt[i];
    }
    wt[0]=0;
    for(i=1;i<n;i++)
    {
        wt[i]=0;
        for(j=0;j<i;j++)
            wt[i]+=bt[j];
    }
    cout<<"\\nProcess\\t\\tBurst Time\\tWaiting Time\\tTurnaround Time";
    for(i=0;i<n;i++)
    {
        tat[i]=bt[i]+wt[i];
        avwt+=wt[i];
        avtat+=tat[i];
        cout<<"\\nP["<<i+1<<"]"<<"\\t\\t"<<bt[i]<<"\\t\\t"<<wt[i]<<"\\t\\t"<<tat[i];
    }
    avwt/=i;
    avtat/=i;
    cout<<"\\n\\nAverage Waiting Time:"<<avwt;
    cout<<"\\nAverage Turnaround Time:"<<avtat;
    cout<<endl;

    return 0;
}



// **************** Output ********************
// Enter number of processes : 3

// Enter Burst Time
// P[1]: 24
// P[2]: 3
// P[3]: 5

// Process         Burst Time      Waiting Time    Turnaround Time
// P[1]            24              0               24
// P[2]            3               24              27
// P[3]            5               27              32

// Average Waiting Time:17
// Average Turnaround Time:27.6667

"""

FIFO = """
#include <iostream>
using namespace std;

int main() {
    int pages[10];
    int n;
    cout << "How many page references do you want to enter : ";
    cin >> n;
    cout << "Enter " << n << " page references : ";
    for (int i = 0; i < n; i++) {
        cin >> pages[i];
    }

    cout << "Page references entered =  ";
    for (int i = 0; i < n; i++) {
        cout << pages[i] << " ";
    }
    cout << endl;

    int capacity = 0, page_faults = 0;
    int frames[10] = {-1}; 
    int frameIndex = 0;

    cout << "Enter the number of frames required : ";
    cin >> capacity;

    for (int i = 0; i < n; i++) {
        int currentPage = pages[i];
        bool pageFound = false;

        for (int j = 0; j < capacity; j++) {
            if (frames[j] == currentPage) {
                pageFound = true;
                break;
            }
        }

        if (!pageFound) {
            if (frameIndex < capacity) {
                frames[frameIndex] = currentPage;
                frameIndex++;
            } else {
                frames[frameIndex % capacity] = currentPage;
                frameIndex++;
            }
            page_faults++;

            cout << "Pass " << page_faults << " = ";
            for (int j = 0; j < capacity; j++) {
                if (frames[j] != -1) {
                    cout << frames[j] << "\\t";
                } else {
                    cout << "E ";
                }
            }
            cout << endl;
        }
    }

    cout << "Page fault:" << page_faults << endl;
    cout << "Page Hit:" << n - page_faults << endl;

    return 0;
}


// **************** Output ********************

//How many page references do you want to enter : 12
// Enter 12 page references : 6 7 8 9 6 7 1 6 7 8 9 1
// Page references entered =  6 7 8 9 6 7 1 6 7 8 9 1 
// Enter the number of frames required : 3
// Pass 1 = 6      0       0
// Pass 2 = 6      7       0
// Pass 3 = 6      7       8
// Pass 4 = 9      7       8
// Pass 5 = 9      6       8
// Pass 6 = 9      6       7
// Pass 7 = 1      6       7
// Pass 8 = 1      8       7
// Pass 9 = 1      8       9
// Page fault:9
// Page Hit:3
"""

LRU = """
#include <iostream>
#include <vector>

using namespace std;

class LRUCache {
private:
    vector<int> cache;
    int capacity;
    int pageFaults;
    int pageHits;

public:
    LRUCache(int cap) : capacity(cap), pageFaults(0), pageHits(0) {}

    void referencePage(int page, int pass) {
        bool found = false;
        for (int i = 0; i < cache.size(); ++i) {
            if (cache[i] == page) {
                found = true;
                cache.erase(cache.begin() + i);
                cache.push_back(page);
                pageHits++;
                break;
            }
        }

        if (!found) {
            pageFaults++;
            if (cache.size() >= capacity) {
                cache.erase(cache.begin());
            }
            cache.push_back(page);
        }
        
        cout << "Pass " << pass << " : ";
        for (int i = 0; i < capacity; ++i) {
            if (i < cache.size()) {
                cout << cache[i] << " ";
            } else {
                cout << "E ";
            }
        }
        cout << endl;
    }

    int getPageFaults() {
        return pageFaults;
    }

    int getPageHits() {
        return pageHits;
    }
};

int main() {
    int n, capacity;
    cout << "Enter the number of page references: ";
    cin >> n;
    cout << "Enter the page reference numbers: ";
    vector<int> pageReferences(n);
    for (int i = 0; i < n; ++i) {
        cin >> pageReferences[i];
    }
    cout << "Enter the capacity of the page table: ";
    cin >> capacity;

    LRUCache cache(capacity);

    for (int i = 0; i < n; ++i) {
        cache.referencePage(pageReferences[i], i + 1);
    }

    cout << "\\nTotal page faults: " << cache.getPageFaults() << endl;
    cout << "Total page hits: " << cache.getPageHits() << endl;

    return 0;
}


// *************** Output ******************

// Enter the number of page references: 15
// Enter the page reference numbers: 6 7 8 9 6 7 1 6 7 8 9 1 7 9 6 
// Enter the capacity of the page table: 3
// Pass 1 : 6 E E 
// Pass 2 : 6 7 E 
// Pass 3 : 6 7 8 
// Pass 4 : 7 8 9 
// Pass 5 : 8 9 6 
// Pass 6 : 9 6 7 
// Pass 7 : 6 7 1 
// Pass 8 : 7 1 6 
// Pass 9 : 1 6 7 
// Pass 10 : 6 7 8 
// Pass 11 : 7 8 9 
// Pass 12 : 8 9 1
// Pass 13 : 9 1 7
// Pass 14 : 1 7 9
// Pass 15 : 7 9 6

// Total page faults: 12
// Total page hits: 3

"""

PRODUCER_CONSUMER = """
#include <iostream>
using namespace std;

int buffer = 0;
const int BUFFER_SIZE = 5;

void producer()
{
    if (buffer == BUFFER_SIZE)
    {
        cout << "Buffer is Full" << endl;
        return;
    }
    ++buffer;
    cout << "Producer produces item " << buffer << endl;
}

void consumer()
{
    if (buffer == 0)
    {
        cout << "Buffer is Empty" << endl;
        return;
    }
    cout << "Consumer consumes item " << buffer << endl;
    --buffer;
}

int main()
{
    int choice;
    while (true)
    {
        cout << "\\n1. Producer\\n2. Consumer\\n3. Exit\\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice)
        {
        case 1:
            producer();
            break;
        case 2:
            consumer();
            break;
        case 3:
            return 0;
        default:
            cout << "Invalid choice!" << endl;
        }
    }

    return 0;
}
"""

ROUND_ROBIN = """
#include<iostream>
using namespace std;

int main() {
    int n, timeSlice, i, x, time, flag = 0;
    float wait_time = 0, turnaround_time = 0;

    cout << "Enter number of processes: ";
    cin >> n;

    x = n;
    int BT[n], AT[n], temp[n];
    int process[n];

    for (int i = 0; i < n; i++)
        process[i] = i;

    cout << "Enter the arrival time of all the processes: \\n";
    for (int i = 0; i < n; i++) {
        cout << "P[" << i << "] = ";
        cin >> AT[i];
    }

    cout << "Enter the Burst time of all the processes: \\n";
    for (int i = 0; i < n; i++) {
        cout << "P[" << i << "] = ";
        cin >> BT[i];
        temp[i] = BT[i];
    }

    cout << "Enter the time slice: ";
    cin >> timeSlice;

    cout << "Process\\t\\tTurnaround Time\\t\\tWaiting Time\\n";
    for (time = 0, i = 0; x != 0;) {
        if (temp[i] <= timeSlice && temp[i] > 0) {
            time += temp[i];
            temp[i] = 0;
            flag = 1;
        } else if (temp[i] > 0) {
            temp[i] -= timeSlice;
            time += timeSlice;
        }

        if (temp[i] == 0 && flag == 1) {
            x--;
            cout << "P[" << i << "] \\t\\t" << time - AT[i] << "\\t\\t\\t" << time - AT[i] - BT[i] << endl;
            wait_time += time - AT[i] - BT[i];
            turnaround_time += time - AT[i];
            flag = 0;
        }

        if (i == n - 1)
            i = 0;
        else if (AT[i + 1] <= time)
            i++;
        else
            i = 0;
    }

    cout << "Average Turnaround Time = " << turnaround_time / n << endl;
    cout << "Average Waiting Time = " << wait_time / n << endl;

    return 0;
}


// **************** Output ********************

// Enter number of processes: 3
// Enter the arrival time of all the processes: 
// P[0] = 0
// P[1] = 0
// P[2] = 0
// Enter the Burst time of all the processes: 
// P[0] = 24
// P[1] = 3
// P[2] = 3
// Enter the time slice: 2
// Process         Turnaround Time         Waiting Time
// P[1]            9                       6
// P[2]            10                      7
// P[0]            30                      6
// Average Turnaround Time = 16.3333
// Average Waiting Time = 6.33333
"""

SJF = """
// Just in Case Pucha toh yeh wala run kar lena
//preemtive
/*
#include <iostream>
using namespace std;

int main() {
    int A[100][5];
    int i, j, n, total = 0, index, temp;
    float avg_wt, avg_tat;

    cout<< "Enter number of processes: ";
    cin >> n;

    cout << "Enter Burst Time and Arrival Time: "<<endl;
    for (i = 0; i < n; i++) {
        cout << "P" << i + 1 << ": ";
        cin >> A[i][1];
        cin >> A[i][4];
        A[i][0] = i + 1;
    }

    for (i = 0; i < n; i++) {
        index = i;
        for (j = i + 1; j < n; j++)
            if (A[j][4] < A[index][4])
                index = j;
        temp = A[i][1];
        A[i][1] = A[index][1];
        A[index][1] = temp;

        temp = A[i][4];
        A[i][4] = A[index][4];
        A[index][4] = temp;

        temp = A[i][0];
        A[i][0] = A[index][0];
        A[index][0] = temp;
    }

    A[0][2] = 0;
    for (i = 1; i < n; i++) {
        A[i][2] = 0;
        for (j = 0; j < i; j++)
            A[i][2] += A[j][1];
        total += A[i][2];
    }

    avg_wt = (float)total / n;
    total = 0;
    cout << "\\nProcess\\tBurst Time\\tArrival Time\\tWaiting Time\\tTurnaround Time" << endl;;

    for (i = 0; i < n; i++) {
        A[i][3] = A[i][1] + A[i][2];
        total += A[i][3];
        cout << "P" << A[i][0] << "\\t" << A[i][1] << "\\t\\t" << A[i][4] << "\\t\\t" << A[i][2] << "\\t\\t" << A[i][3] << endl;
    }

    avg_tat = (float)total / n;
    cout << "Average Waiting Time= " << avg_wt << endl;
    cout << "Average Turnaround Time= " << avg_tat << endl;
}
*/


//non preemtive
#include <iostream>
using namespace std;

int main() {
    int A[100][4];
    int i, j, n, total = 0, index, temp;
    float avg_wt, avg_tat;

    cout << "Enter number of process: ";
    cin >> n;

    cout << "Enter Burst Time:" << endl;
    for (i = 0; i < n; i++) {
        cout << "P" << i + 1 << ": ";
        cin >> A[i][1];
        A[i][0] = i + 1;
    }
    for (i = 0; i < n; i++) {
        index = i;
        for (j = i + 1; j < n; j++)
            if (A[j][1] < A[index][1])
                index = j;
        temp = A[i][1];
        A[i][1] = A[index][1];
        A[index][1] = temp;

        temp = A[i][0];
        A[i][0] = A[index][0];
        A[index][0] = temp;
    }

    A[0][2] = 0;
    for (i = 1; i < n; i++) {
        A[i][2] = 0;
        for (j = 0; j < i; j++)
            A[i][2] += A[j][1];
        total += A[i][2];
    }

    avg_wt = (float)total / n;
    total = 0;
    cout<<"\\nProcess\\t\\tBurst Time\\tWaiting Time\\tTurnaround Time"<<endl;;


    for (i = 0; i < n; i++) {
        A[i][3] = A[i][1] + A[i][2];
        total += A[i][3];
        cout << "P" << A[i][0] << "                    " << A[i][1] << "              " << A[i][2] << "              " << A[i][3] << endl;
    }

    avg_tat = (float)total / n;
    cout << "Average Waiting Time= " << avg_wt << endl;
    cout << "Average Turnaround Time= " << avg_tat << endl;
}


// ******************* Output **********************

// Enter number of process: 3
// Enter Burst Time:
// P1: 24
// P2: 3
// P3: 5

// Process         Burst Time      Waiting Time    Turnaround Time
// P2                    3              0              3
// P3                    5              3              8
// P1                    24              8              32
// Average Waiting Time= 3.66667
// Average Turnaround Time= 14.3333
"""

DYNAMIC_PARTITION = """
#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

struct Partition {
    int base;
    int size;
};

void displayMemoryDetails(int memorySize, int sum) {
    cout << "Total Memory = " << memorySize << endl;
    cout << "Used Memory = " << sum << endl;
    cout << "Remaining Memory = " << memorySize - sum << endl;
}

void displayPartitionDetails(Partition partitions[], int numPartitions) {
    cout << "Partition Number\\tPartition Base\\t\\tPartition Size\\n";
    for (int i = 0; i < numPartitions; i++) {
        cout << i + 1 << "\\t\\t\\t" << partitions[i].base << "\\t\\t\\t" << partitions[i].size << endl;
    }
}

int getProcesses(int processes[], Partition partitions[], int memorySize, int numProcesses) {
    int sum = 0;
    int base = 0; // Initialize base address for partitions
    for (int i = 0; i < numProcesses; i++) {
        cout << "Enter the size of process " << i + 1 << ": ";
        cin >> processes[i];
        if (processes[i] > memorySize) {
            cout << "Error: The size of the process is greater than the available memory!" << endl;
            return 0;
        }
        sum += processes[i];
        partitions[i].base = base;
        partitions[i].size = processes[i];
        base += processes[i];
    }
    return sum;
}

int main() {
    int memorySize, numProcesses, sum = 0;

    cout << "Enter the size of memory: ";
    cin >> memorySize;

    cout << "How many processes you want to add? - ";
    cin >> numProcesses;

    int processes[numProcesses];
    Partition partitions[numProcesses];

    while (true) {
        sum = getProcesses(processes, partitions, memorySize, numProcesses);
        if (sum != 0) {
            break;
        }
    }

    if (sum > memorySize) {
        cout << "Error: The total memory of the processes is greater than the available memory!" << endl;
        return 1;
    }

    displayMemoryDetails(memorySize, sum);
    displayPartitionDetails(partitions, numProcesses);
    cout << endl;

    return 0;
}


"""

STATIC_PARTITION = """
#include<iostream>
using namespace std;

int main()
{
    int total_size = 0, num_partitions = 0, partition_size;
    string partstatus = "";

    cout << "Define the static size of the partition: "<<endl;
    cin >> total_size;

    cout << "How many partitions do you want to allocate? ";
    cin >> num_partitions;
    int partitionbase=0;

    for (int i = 1; i <= num_partitions; i++)
    {
        cout << "Enter the size of the " << i << "th partition: ";
        cin >> partition_size;

        if (partition_size > total_size)
        {
            cout << "No space for the " << i << "th partition" << endl;
            partstatus = "unallocated";
            cout << "Partition number\\tPartition base\\tPartition size\\tPartition status" << endl;
            cout << "\\t" << i << "\\t\\t" << partitionbase << "\\t\\t" << partition_size << "\\t\\t" << partstatus << endl;
            break;  
        }
        else
        {
            total_size -= partition_size;
            cout << "Space left: " << total_size << endl;
            partstatus = "allocated";
        }
        cout << "Partition number\\tPartition base\\tPartition size\\tPartition status" << endl;
        cout << "\\t" << i << "\\t\\t" << partitionbase << "\\t\\t" << partition_size << "\\t\\t" << partstatus << endl;
        partitionbase+=partition_size;
    }


}
"""

CESEAR_CIPHER = """
#include <iostream>
#include <cctype> // for isalnum

using namespace std;

void encrypt();
void decrypt();

int main() {
    int choice;
    do {
        cout << "Enter Choice :\\n";
        cout << "1: Encrypt\\n";
        cout << "2: Decrypt\\n";
        cout << "0: Exit\\n";

        cin >> choice;

        switch (choice) {
            case 1:
                encrypt();
                break; 
            case 2: 
                decrypt();
                break; 
            case 0:
                cout << "Exiting program.\\n";
                break;
            default:
                cout << "Wrong Choice\\n";
        }

    } while (choice != 0);

    return 0;
}

void encrypt() {
    string text;
    char ch;
    int key;

    cout << "Enter a message to encrypt: ";
    cin.ignore(); 
    getline(cin, text);  

    cout << "Enter the key: ";
    cin >> key;

    for (size_t i = 0; i < text.length(); ++i) {
        ch = text[i];
        if (isalnum(ch)) {
            if (islower(ch)) {
                ch = ((ch - 'a' + key) % 26 + 26) % 26 + 'a';
            }
            if (isupper(ch)) {
                ch = ((ch - 'A' + key) % 26 + 26) % 26 + 'A';
            }
            if (isdigit(ch)) {
                ch = ((ch - '0' + key) % 10 + 10) % 10 + '0';
            }
        }
        else {
            cout << "Invalid Message\\n";
            return;
        }
        text[i] = ch;
    }
    cout << "Encrypted message: " << text << endl;
}

void decrypt() {
    string text;
    char ch;
    int key;

    cout << "Enter a message to decrypt: ";
    cin.ignore(); 
    getline(cin, text);  

    cout << "Enter the key: ";
    cin >> key;

    for (size_t i = 0; i < text.length(); ++i) {
        ch = text[i];
        if (isalnum(ch)) {
            if (islower(ch)) {
                ch = ((ch - 'a' - key) % 26 + 26) % 26 + 'a';
            }
            if (isupper(ch)) {
                ch = ((ch - 'A' - key) % 26 + 26) % 26 + 'A';
            }
            if (isdigit(ch)) {
                ch = ((ch - '0' - key) % 10 + 10) % 10 + '0';
            }
        }
        else {
            cout << "Invalid Message\\n";
            return;
        }
        text[i] = ch;
    }
    cout << "Decrypted message: " << text << endl;
}
"""

FILE_COPY = """
    #include <iostream>
#include <fstream>

using namespace std;

int main() {

    ifstream file1Read("file1.txt");

    if (!file1Read.is_open()) {
        cerr << "Error opening file1.txt for reading." << endl;
        return 1;
    }

    ofstream file2("file2.txt");

    if (!file2.is_open()) {
        cerr << "Error opening file2.txt for writing." << endl;
        return 1;
    }

    char ch;
    while (file1Read.get(ch)) {
        file2.put(  ch);
    }

    file2.close();
    file1Read.close();

   cout << "Content copied from file1.txt to file2.txt successfully." << endl;

    return 0;
}

"""

FILE_CREATE_AND_OPEN = """
#include <iostream>
#include <fstream>

using namespace std;
int main() {

    ofstream myfile("example.txt");
    if (myfile.is_open()) {
        myfile.close();

        cout << "File created and written successfully." << endl;
    } else {
        cout  << "Unable to open the file." << endl;
    }

    return 0;
}
"""

FILE_READ = """
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    ifstream inputFile("read.txt", ios::in);

    if (inputFile.is_open()) {
        string line;
        while (getline(inputFile, line)) {
            cout << line << endl;
        }
        inputFile.close();
    } else {
        cout << "Unable to open the file" << endl;
        return 1;
    }

    return 0;
}

"""

FILE_WRITE = """
#include <iostream>
#include <fstream>

using namespace std;
int main() {

    ofstream myfile("write.txt");
    if (myfile.is_open()) {

        myfile << "Hello, this is a simple file created and opened in C++!" <<endl;
        myfile << "You can add more text or modify it as needed." <<endl;

        myfile.close();

        cout << "File created and written successfully." << endl;
    } else {
        cout  << "Unable to open the file." << endl;
    }

    return 0;
}

"""

def code():
    while (True):
        print("\nSelect Your Option : \n")
        print("1.System Calls")
        print("2.FCFS")
        print("3.ROUND ROBIN")
        print("4.SJF")
        print("5.Producer Consumer")
        print("6.BANKERS")
        print("7.STATIC PARTITION")
        print("8.DYNAMIC PARTITION")
        print("9.FIFO")
        print("10.LRU")
        print("11.FCFS AND SSTF DISK SCHEDULING")

        try:
            c = int(input("Enter Your Option : "))
        except:
             print("\nNumber Barobar Dal\nIder Bhi Error Create kar ra hai")

        match c:
            case 1:
                print("4 Files are Downloaded")
                with open("FILE_COPY.cpp", "w") as f:
                    f.write(FILE_COPY)
                with open("FILE_CREATE_AND_OPEN.cpp", "w") as f:
                    f.write(FILE_CREATE_AND_OPEN)
                with open("FILE_READ.cpp", "w") as f:
                    f.write(FILE_READ)
                with open("FILE_WRITE.cpp", "w") as f:
                    f.write(FILE_WRITE)

            case 2:
                with open("FCFS.cpp", "w") as f:
                    f.write(FCFS)
            case 3:
                with open("ROUND_ROBIN.cpp", "w") as f:
                    f.write(ROUND_ROBIN)
            case 4:
                with open("SJF.cpp", "w") as f:
                    f.write(SJF)
            case 5:
                with open("PRODUCER_CONSUMER.cpp", "w") as f:
                    f.write(PRODUCER_CONSUMER)
            case 6:
                with open("Bankers.cpp", "w") as f:
                    f.write(Bankers)
            case 7:
                with open("STATIC_PARTITION.cpp", "w") as f:
                    f.write(STATIC_PARTITION)
            case 8:
                with open("DYNAMIC_PARTITION.cpp", "w") as f:
                    f.write(DYNAMIC_PARTITION)
            case 9:
                with open("FIFO.cpp", "w") as f:
                    f.write(FIFO)
            case 10:
                with open("LRU.cpp", "w") as f:
                    f.write(LRU)
            case 11:
                with open("FCFS_SSTF.cpp", "w") as f:
                    f.write(FCFS_AND_SSTF)
            case _:
                print("\nNumber toh Barobar Dal\nIder Bhi Error Create kar ra hai")
