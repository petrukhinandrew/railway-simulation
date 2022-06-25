#include <stdio.h>
#include <stdlib.h>

int main() {
	int listA[30];
	int listB[30];
	for (int i = 0; i < 30; ++i) {
		listA[i] = rand() % 10;
		listB[i] = rand() % 10;
	}

	int listA_count[9];
	int listB_count[9];
	for (int i = 0; i < 9; ++i) {
		listA_count[i] = 0;
		listB_count[i] = 0;
	}
	for (int i = 0; i < 30; ++i) {
		listA_count[listA[i]]++;
		listB_count[listB[i]]++;
	}
	int listA_uniq = 0, listB_mult = 0;
	for (int i = 0; i < 9; ++i) {
		if (listA_count[i] == 1)
			listA_uniq++;
		if (listB_count[i] > 1)
			listB_mult++;
	}
	int mergedB[30 + listA_uniq], mergedA[30 + listB_mult];
	memcpy(mergedB, listB, 120);
	
	listA_uniq = 0;
	listB_mult = 0;
	for (int i = 0; i < 9; ++i) {
		if (listA_count[i] == 1) {
			mergedB[30 + listA_uniq] = i;
			listA_uniq++;
		}
		if (listB_count[i] > 1) {
			mergedA[listB_mult] = i;
			listB_mult++;
		}
	}

	memcpy(mergedA + listB_mult, listA, 120);
	
	for (int i = 0; i < 30 + listB_mult; ++i) {
		printf("%d ", mergedA[i]);
	}
	printf("\n");
	for (int i = 0; i < 30 + listA_uniq; ++i) {
		printf("%d ", mergedB[i]);
	}				
	return 0;
}
