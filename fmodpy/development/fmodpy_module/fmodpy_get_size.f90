PROGRAM GET_SIZE
  USE SIMPLE_TEST
  USE ISO_FORTRAN_ENV, ONLY: REAL64, INT64
  INTEGER(KIND=INT64) :: MULT_B
  REAL :: MULT_A
  PRINT *, SIZEOF(MULT_B)
  PRINT *, SIZEOF(MULT_A)
END PROGRAM GET_SIZE