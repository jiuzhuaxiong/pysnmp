# PySNMP SMI module. Autogenerated from smidump -f python PYSNMP-SOURCE-MIB
# by libsmi2pysnmp-0.1.3 at Fri Jan 16 17:45:19 2015,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( pysnmpModuleIDs, ) = mibBuilder.importSymbols("PYSNMP-MIB", "pysnmpModuleIDs")
( snmpTargetAddrEntry, ) = mibBuilder.importSymbols("SNMP-TARGET-MIB", "snmpTargetAddrEntry")
( Bits, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( TAddress, ) = mibBuilder.importSymbols("SNMPv2-TC", "TAddress")

# Objects

pysnmpSourceMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 20408, 3, 1, 8)).setRevisions(("2015-01-16 00:00",))
if mibBuilder.loadTexts: pysnmpSourceMIB.setOrganization("SNMP Laboratories")
if mibBuilder.loadTexts: pysnmpSourceMIB.setContactInfo("E-mail:     info@snmplabs.com\nSubscribe:  pysnmp-users-request@lists.sourceforge.net")
if mibBuilder.loadTexts: pysnmpSourceMIB.setDescription("This MIB module defines implementation specific objects\nthat provide variable source transport endpoints feature to\nSNMP Engine and Applications.")
pysnmpSourceMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 3, 1, 8, 1))
snmpSourceAddrTable = MibTable((1, 3, 6, 1, 4, 1, 20408, 3, 1, 8, 1, 1))
if mibBuilder.loadTexts: snmpSourceAddrTable.setDescription("A table of transport addresses to be used as a source in the\ngeneration of SNMP messages. This table contains additional\nobjects for the SNMP-TRANSPORT-ADDRESS::snmpSourceAddressTable.")
snmpSourceAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 20408, 3, 1, 8, 1, 1, 1))
if mibBuilder.loadTexts: snmpSourceAddrEntry.setDescription("A transport address to be used as a source in the generation\nof SNMP operations.\n\nAn entry containing additional management information\napplicable to a particular target.")
snmpSourceAddrTAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 20408, 3, 1, 8, 1, 1, 1, 1), TAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpSourceAddrTAddress.setDescription("This object contains a transport address.  The format of\nthis address depends on the value of the\nsnmpSourceAddrTDomain object.")
pysnmpSourceMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 3, 1, 8, 2))
pysnmpSourceMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 3, 1, 8, 2, 1))
pysnmpSourceMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 3, 1, 8, 2, 2))

# Augmentions
snmpTargetAddrEntry, = mibBuilder.importSymbols("SNMP-TARGET-MIB", "snmpTargetAddrEntry")
snmpTargetAddrEntry.registerAugmentions(("PYSNMP-SOURCE-MIB", "snmpSourceAddrEntry"))
snmpSourceAddrEntry.setIndexNames(*snmpTargetAddrEntry.getIndexNames())

# Exports

# Module identity
mibBuilder.exportSymbols("PYSNMP-SOURCE-MIB", PYSNMP_MODULE_ID=pysnmpSourceMIB)

# Objects
mibBuilder.exportSymbols("PYSNMP-SOURCE-MIB", pysnmpSourceMIB=pysnmpSourceMIB, pysnmpSourceMIBObjects=pysnmpSourceMIBObjects, snmpSourceAddrTable=snmpSourceAddrTable, snmpSourceAddrEntry=snmpSourceAddrEntry, snmpSourceAddrTAddress=snmpSourceAddrTAddress, pysnmpSourceMIBConformance=pysnmpSourceMIBConformance, pysnmpSourceMIBCompliances=pysnmpSourceMIBCompliances, pysnmpSourceMIBGroups=pysnmpSourceMIBGroups)

