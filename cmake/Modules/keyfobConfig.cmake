INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_KEYFOB keyfob)

FIND_PATH(
    KEYFOB_INCLUDE_DIRS
    NAMES keyfob/api.h
    HINTS $ENV{KEYFOB_DIR}/include
        ${PC_KEYFOB_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    KEYFOB_LIBRARIES
    NAMES gnuradio-keyfob
    HINTS $ENV{KEYFOB_DIR}/lib
        ${PC_KEYFOB_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/keyfobTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(KEYFOB DEFAULT_MSG KEYFOB_LIBRARIES KEYFOB_INCLUDE_DIRS)
MARK_AS_ADVANCED(KEYFOB_LIBRARIES KEYFOB_INCLUDE_DIRS)
