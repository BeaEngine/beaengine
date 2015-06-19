# unit tests

## requirements (debian/ubuntu)

```
apt-get install python-nose
```

## howto (debian/ubuntu)

```
cd ~ & beaengine & cmake 
cmake -DoptHAS_OPTIMIZED=TRUE -DoptHAS_SYMBOLS=TRUE -DoptBUILD_64BIT=FALSE -DoptBUILD_DLL=TRUE -DoptBUILD_LITE=FALSE beaengine
make
cp beaengine/lib/Linux.gnu.relwithdebinfo/libBeaEngine.so beaengine/headers
nosetests tests
```


